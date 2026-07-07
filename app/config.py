import json
import os

CONFIG_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'config.json')

DEFAULT_CONFIG = {
    "twitch_token": "oauth:ваш_токен",
    "twitch_nick": "ваш_бот",
    "twitch_channel": "ваш_канал",
    "piper_exe": "piper/piper.exe",
    "default_model": "voices/ru_RU-irina-medium.onnx",  # голос по умолчанию
    "role_models": {
        "moderator": "voices/ru_RU-denis-medium.onnx",
        "subscriber": "voices/ru_RU-irina-medium.onnx",
        "vip": "voices/ru_RU-irina-medium.onnx",
        "broadcaster": "voices/ru_RU-irina-medium.onnx"
    },
    "mic_device_id": None,
    "rms_threshold": 0.015,
    "silence_delay": 0.5,
    "silence_enabled": True,
    "speech_speed": 0.8,
    "ignored_users": ["streamelements", "nightbot", "fossabot", "moobot"],
    "max_queue_size": 15,
    "message_max_len": 150,
    "mute_hotkey": "ctrl+shift+m"
}

def load_config():
    if not os.path.exists(CONFIG_PATH):
        save_config(DEFAULT_CONFIG)
        return DEFAULT_CONFIG.copy()
    with open(CONFIG_PATH, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_config(config):
    with open(CONFIG_PATH, 'w', encoding='utf-8') as f:
        json.dump(config, f, indent=4, ensure_ascii=False)