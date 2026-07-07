from flask import Flask, render_template, request, jsonify
import threading
import webbrowser
import config
import os

app = Flask(__name__, template_folder='templates')
bot_instance = None

@app.route('/')
def index():
    cfg = config.load_config()
    return render_template('settings.html', config=cfg)

@app.route('/save', methods=['POST'])
def save():
    cfg = config.load_config()
    cfg['twitch_token'] = request.form.get('twitch_token', '').strip()
    cfg['twitch_nick'] = request.form.get('twitch_nick', '').strip()
    cfg['twitch_channel'] = request.form.get('twitch_channel', '').strip()
    cfg['piper_exe'] = request.form.get('piper_exe', '').strip()
    cfg['default_model'] = request.form.get('default_model', '').strip()

    # Сохраняем модели для ролей
    cfg['role_models'] = {
        'moderator': request.form.get('moderator_model', '').strip(),
        'subscriber': request.form.get('subscriber_model', '').strip(),
        'vip': request.form.get('vip_model', '').strip(),
        'broadcaster': request.form.get('broadcaster_model', '').strip()
    }

    mic_id = request.form.get('mic_device_id', '').strip()
    cfg['mic_device_id'] = int(mic_id) if mic_id.isdigit() else None

    cfg['rms_threshold'] = float(request.form.get('rms_threshold', 0.015))
    cfg['silence_delay'] = float(request.form.get('silence_delay', 0.5))
    cfg['silence_enabled'] = request.form.get('silence_enabled') == 'on'
    cfg['speech_speed'] = float(request.form.get('speech_speed', 1.0))

    cfg['max_queue_size'] = int(request.form.get('max_queue_size', 15))
    cfg['message_max_len'] = int(request.form.get('message_max_len', 150))

    ignored_raw = request.form.get('ignored_users', '')
    cfg['ignored_users'] = [u.strip() for u in ignored_raw.replace(',', ' ').split() if u.strip()]

    config.save_config(cfg)
    if bot_instance:
        bot_instance.reload_config()

    return jsonify({'status': 'ok'})

@app.route('/api/models')
def get_models():
    """Возвращает список всех .onnx файлов в папке voices"""
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    voices_dir = os.path.join(base_dir, 'voices')
    models = []
    if os.path.exists(voices_dir):
        for file in os.listdir(voices_dir):
            if file.endswith('.onnx'):
                # Возвращаем полный относительный путь voices/имя_файла.onnx
                models.append(os.path.join('voices', file))
    return jsonify(models)

def run_server():
    threading.Timer(1.0, lambda: webbrowser.open('http://127.0.0.1:5000')).start()
    app.run(host='127.0.0.1', port=5000, debug=False, use_reloader=False)