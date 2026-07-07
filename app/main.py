import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import asyncio
import queue
import threading
import re
import subprocess
import time
import unicodedata
import numpy as np
import sounddevice as sd
import keyboard
from twitchio import Client

import config
import web_ui

# --- Загрузка конфига ---
cfg = config.load_config()
message_queue = queue.Queue()
is_muted = False
is_streamer_speaking = False
rms_lock = threading.Lock()
bot_instance = None

# EMERGENCY STOP: флаг для экстренной остановки
emergency_stop = False
emergency_lock = threading.Lock()

def reload_config():
    global cfg
    cfg = config.load_config()
    print("✅ Конфиг перезагружен")

# --- Определение модели по роли ---
def get_model_for_role(role):
    """Возвращает путь к модели для указанной роли, или default_model если роль не найдена."""
    role_models = cfg.get('role_models', {})
    model = role_models.get(role)
    if model and os.path.exists(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), model)):
        return model
    return cfg.get('default_model', 'voices/ru_RU-irina-medium.onnx')

# --- Функция озвучивания с выбором модели и поддержкой экстренной остановки ---
def generate_speech(text, model_path=None):
    global emergency_stop

    # Очистка текста
    text = ''.join(ch for ch in text if unicodedata.category(ch)[0] != 'C')
    text = text.encode('utf-8', errors='replace').decode('utf-8')
    if len(text) > 150:
        text = text[:150] + "..."

    output_wav = "temp_speech.wav"
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    piper_exe = os.path.join(base_dir, cfg['piper_exe'])
    
    if model_path is None:
        model_path = cfg.get('default_model', 'voices/ru_RU-irina-medium.onnx')
    if not os.path.isabs(model_path):
        model_path = os.path.join(base_dir, model_path)

    speed = cfg.get('speech_speed', 1.0)
    cmd = [
        piper_exe,
        "--model", model_path,
        "--output_file", output_wav,
        "--length_scale", str(speed)
    ]
    print(f"🔧 Piper команда: {' '.join(cmd)}")
    print(f"📝 Текст: {text[:50]}...")
    try:
        result = subprocess.run(
            cmd,
            input=text.encode('utf-8'),
            capture_output=True,
            timeout=15
        )
        print(f"Код возврата: {result.returncode}")
        if result.stderr:
            print("STDERR:", result.stderr.decode('utf-8', errors='replace'))
        if result.returncode != 0:
            print("❌ Piper завершился с ошибкой")
            return
        if os.path.exists(output_wav):
            size = os.path.getsize(output_wav)
            print(f"✅ Файл создан, размер: {size} байт")
            if size < 10000:
                print("⚠️ Файл слишком мал, нет аудиоданных.")
                return
        else:
            print("❌ Файл не создан")
            return
    except subprocess.TimeoutExpired:
        print("❌ Piper завис")
        return
    except Exception as e:
        print(f"❌ Исключение: {e}")
        return

    # --- Воспроизведение через pygame с поддержкой экстренной остановки ---
    try:
        import pygame
        pygame.mixer.init()
        pygame.mixer.music.load(output_wav)
        pygame.mixer.music.play()
        print("▶️ Воспроизведение началось. Нажмите Ctrl+Shift+E для экстренной остановки.")
        # Цикл ожидания окончания воспроизведения с проверкой флага
        while pygame.mixer.music.get_busy():
            time.sleep(0.1)
            with emergency_lock:
                if emergency_stop:
                    # Сработала экстренная остановка
                    pygame.mixer.music.stop()
                    print("🛑 Воспроизведение прервано экстренной остановкой!")
                    # Очищаем очередь
                    while not message_queue.empty():
                        try:
                            message_queue.get_nowait()
                        except queue.Empty:
                            break
                    print("🗑️ Очередь очищена.")
                    # Удаляем временный файл, если он есть
                    if os.path.exists(output_wav):
                        try:
                            os.remove(output_wav)
                            print("🗑️ Временный файл удалён.")
                        except Exception as e:
                            print(f"⚠️ Не удалось удалить файл: {e}")
                    # Сбрасываем флаг, чтобы не остановить следующее воспроизведение
                    emergency_stop = False
                    return
        pygame.mixer.music.stop()
        pygame.mixer.quit()
        print("✅ Воспроизведение завершено")
    except ImportError:
        # Если pygame не установлен, используем os.startfile (без поддержки остановки)
        try:
            os.startfile(output_wav)
            time.sleep(2)
            print("✅ Воспроизведение через os.startfile")
        except Exception as e:
            print(f"Ошибка воспроизведения: {e}")
    except Exception as e:
        print(f"Ошибка воспроизведения: {e}")

    # --- Безопасное удаление файла ---
    if os.path.exists(output_wav):
        for attempt in range(5):
            try:
                time.sleep(0.2)
                os.remove(output_wav)
                print("🗑️ Временный файл удалён")
                break
            except PermissionError:
                print(f"⏳ Попытка {attempt+1}: файл занят, ждём...")
                time.sleep(0.3)
        else:
            print("⚠️ Не удалось удалить файл.")

# --- Микрофон ---
def audio_callback(indata, frames, time, status):
    global is_streamer_speaking
    if not cfg.get('silence_enabled', True):
        return
    rms = np.sqrt(np.mean(indata[:, 0] ** 2))
    with rms_lock:
        is_streamer_speaking = (rms > cfg['rms_threshold'])

def start_microphone_listener():
    global is_streamer_speaking
    if not cfg.get('silence_enabled', True):
        print("ℹ️ Режим тишины отключён, микрофон не используется.")
        return

    try:
        stream = sd.InputStream(
            device=cfg['mic_device_id'],
            channels=1,
            samplerate=16000,
            callback=audio_callback,
            blocksize=512
        )
        stream.start()
        print("✅ Микрофон слушается (режим тишины включён).")
        while True:
            time.sleep(1)
            if not cfg.get('silence_enabled', True):
                print("ℹ️ Режим тишины отключён, остановка захвата микрофона.")
                stream.stop()
                stream.close()
                break
    except Exception as e:
        print(f"⚠️ Ошибка микрофона: {e}. Режим тишины недоступен.")

# --- Поток озвучивания ---
def speaker_worker():
    global is_muted, is_streamer_speaking
    while True:
        item = message_queue.get()
        if item is None:
            break
        if isinstance(item, tuple):
            text, model_path = item
        else:
            text = item
            model_path = None

        if is_muted:
            print("🔇 Режим мута включен. Сообщение пропущено.")
            continue

        if cfg.get('silence_enabled', True):
            with rms_lock:
                speaking_now = is_streamer_speaking
            if speaking_now:
                print("🎙️ Стример говорит, ждём паузы...")
                silent_seconds = 0
                while True:
                    with rms_lock:
                        if is_streamer_speaking:
                            silent_seconds = 0
                        else:
                            silent_seconds += 0.2
                    if silent_seconds >= cfg['silence_delay']:
                        break
                    time.sleep(0.2)

        print(f"Говорю: {text} (модель: {model_path or 'default'})")
        generate_speech(text, model_path)

# --- Класс бота Twitch ---
class StreamBot(Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ignored_users = cfg['ignored_users']
        self.max_queue = cfg['max_queue_size']
        self.max_len = cfg['message_max_len']

    async def event_ready(self):
        print(f'✅ Бот {self.nick} подключен к каналу {cfg["twitch_channel"]}')

    async def event_message(self, message):
        author = message.author.name.lower()
        if author in self.ignored_users or author == self.nick.lower():
            return

        # Определяем роль пользователя
        role = None
        if message.author.is_broadcaster:
            role = 'broadcaster'
        elif message.author.is_mod:
            role = 'moderator'
        elif message.author.is_vip:
            role = 'vip'
        elif message.author.is_subscriber:
            role = 'subscriber'

        model_path = None
        if role:
            model_path = get_model_for_role(role)

        clean_text = message.content
        clean_text = re.sub(r'http\S+|www\.\S+', '[ссылка]', clean_text)
        clean_text = re.sub(r'@\w+', '', clean_text)
        clean_text = re.sub(r'![\w]+', '', clean_text)
        clean_text = re.sub(r'[^\w\s.,!?-]', '', clean_text)
        if len(clean_text) > self.max_len:
            clean_text = clean_text[:self.max_len] + "..."
        if len(clean_text.strip()) == 0:
            return

        if message_queue.qsize() >= self.max_queue:
            try:
                message_queue.get_nowait()
            except queue.Empty:
                pass
        message_queue.put((clean_text, model_path))
        print(f"📩 В очереди ({message_queue.qsize()}): {clean_text} (роль: {role or 'зритель'})")

    def reload_config(self):
        global cfg
        cfg = config.load_config()
        self.ignored_users = cfg['ignored_users']
        self.max_queue = cfg['max_queue_size']
        self.max_len = cfg['message_max_len']
        print("✅ Настройки бота обновлены")

# --- Обработчик горячей клавиши для мьюта ---
def toggle_mute():
    global is_muted
    is_muted = not is_muted
    print(f"🔊 Звук {'ВЫКЛЮЧЕН' if is_muted else 'ВКЛЮЧЕН'}")

# --- EMERGENCY STOP: функция экстренной остановки ---
def emergency_stop_handler():
    global emergency_stop
    with emergency_lock:
        # Устанавливаем флаг, чтобы прервать текущее воспроизведение
        emergency_stop = True
        # Если воспроизведение не идёт, очищаем очередь немедленно
        try:
            # Попытка остановить pygame, если он инициализирован и играет
            import pygame
            if pygame.mixer.get_init():
                pygame.mixer.music.stop()
        except:
            pass
        # Очищаем очередь в любом случае
        while not message_queue.empty():
            try:
                message_queue.get_nowait()
            except queue.Empty:
                break
        # Удаляем временный файл, если он есть
        if os.path.exists("temp_speech.wav"):
            try:
                os.remove("temp_speech.wav")
            except Exception as e:
                print(f"⚠️ Не удалось удалить файл при аварийной остановке: {e}")
        print("🛑 Аварийная остановка выполнена! Очередь очищена, воспроизведение прервано.")

# --- ЗАПУСК ---
if __name__ == "__main__":
    if cfg.get('silence_enabled', True):
        mic_thread = threading.Thread(target=start_microphone_listener, daemon=True)
        mic_thread.start()
    else:
        print("ℹ️ Режим тишины отключён в настройках. Микрофон не используется.")

    speech_thread = threading.Thread(target=speaker_worker, daemon=True)
    speech_thread.start()

    # Горячие клавиши
    keyboard.add_hotkey(cfg.get('mute_hotkey', 'ctrl+shift+m'), toggle_mute)
    # EMERGENCY STOP: Ctrl+Shift+E
    keyboard.add_hotkey('ctrl+shift+e', emergency_stop_handler)

    web_thread = threading.Thread(target=web_ui.run_server, daemon=True)
    web_thread.start()

    bot = StreamBot(
        token=cfg['twitch_token'],
        initial_channels=[cfg['twitch_channel']]
    )
    web_ui.bot_instance = bot

    try:
        bot.run()
    except KeyboardInterrupt:
        print("Завершение...")