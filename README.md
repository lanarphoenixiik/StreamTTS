<!-- README.md в формате HTML (совместим с GitHub) -->

<h1 align="center" style="color: #f0f6fc; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif; font-weight: 600; font-size: 2.5em; margin-bottom: 0.2em;">
  🎙️ StreamTTS Portable v1.0
</h1>

<p align="center" style="margin-top: 0;">
  <a href="https://github.com/lanarphoenixiik/StreamTTS/releases">
    <img src="https://img.shields.io/badge/version-1.0-blue" alt="Version" style="margin-right: 5px;">
  </a>
  <a href="#">
    <img src="https://img.shields.io/badge/platform-Windows-lightgrey" alt="Platform" style="margin-right: 5px;">
  </a>
  <a href="#">
    <img src="https://img.shields.io/badge/license-MIT-green" alt="License">
  </a>
</p>

<p align="center" style="color: #c9d1d9; font-size: 1.1em; max-width: 700px; margin: 0 auto 20px auto; line-height: 1.6;">
  <strong style="color: #f0f6fc;">Умная озвучка чата Twitch с разными голосами для ролей — всё локально, бесплатно и портативно</strong>
</p>

<blockquote style="background: #0d1117; border-left: 4px solid #58a6ff; padding: 10px 20px; border-radius: 4px; color: #c9d1d9; font-style: italic;">
  ⚡ <strong>Одним предложением:</strong> Автоматически читает сообщения из чата Twitch голосом, используя локальный синтезатор речи, с возможностью назначать разные голоса для модераторов, подписчиков, VIP и самого стримера.
</blockquote>

<hr style="border: none; border-top: 1px solid #30363d; margin: 30px 0;">

<h2 style="color: #f0f6fc; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif; font-weight: 500; font-size: 1.8em;">
  📋 Содержание
</h2>

<ul style="color: #c9d1d9; font-size: 1.05em; line-height: 1.8; columns: 2; list-style: none; padding-left: 0;">
  <li style="padding: 4px 0;">· <a href="#-особенности" style="color: #58a6ff; text-decoration: none;">✨ Особенности</a></li>
  <li style="padding: 4px 0;">· <a href="#%EF%B8%8F-системные-требования" style="color: #58a6ff; text-decoration: none;">🖥️ Системные требования</a></li>
  <li style="padding: 4px 0;">· <a href="#-быстрый-старт" style="color: #58a6ff; text-decoration: none;">🚀 Быстрый старт</a></li>
  <li style="padding: 4px 0;">· <a href="#%EF%B8%8F-веб-интерфейс" style="color: #58a6ff; text-decoration: none;">🎛️ Веб-интерфейс</a></li>
  <li style="padding: 4px 0;">· <a href="#-голосовые-модели" style="color: #58a6ff; text-decoration: none;">🎭 Голосовые модели</a></li>
  <li style="padding: 4px 0;">· <a href="#%EF%B8%8F-горячие-клавиши" style="color: #58a6ff; text-decoration: none;">⌨️ Горячие клавиши</a></li>
  <li style="padding: 4px 0;">· <a href="#%EF%B8%8F-конфигурация" style="color: #58a6ff; text-decoration: none;">⚙️ Конфигурация</a></li>
  <li style="padding: 4px 0;">· <a href="#-устранение-проблем" style="color: #58a6ff; text-decoration: none;">🧠 Устранение проблем</a></li>
  <li style="padding: 4px 0;">· <a href="#-структура-проекта" style="color: #58a6ff; text-decoration: none;">📁 Структура проекта</a></li>
  <li style="padding: 4px 0;">· <a href="#-лицензия" style="color: #58a6ff; text-decoration: none;">📜 Лицензия</a></li>
</ul>

<hr style="border: none; border-top: 1px solid #30363d; margin: 30px 0;">

<h2 id="-особенности" style="color: #f0f6fc; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif; font-weight: 500; font-size: 1.8em;">
  ✨ Особенности
</h2>

<table style="width: 100%; border-collapse: collapse; background: #0d1117; border-radius: 8px; overflow: hidden; color: #c9d1d9; font-size: 0.95em;">
  <thead>
    <tr style="background: #161b22;">
      <th style="padding: 12px 15px; text-align: left; font-weight: 600; border-bottom: 1px solid #30363d;">Функция</th>
      <th style="padding: 12px 15px; text-align: left; font-weight: 600; border-bottom: 1px solid #30363d;">Описание</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="padding: 10px 15px; border-bottom: 1px solid #21262d;">🗣️ <strong>Озвучка чата</strong></td><td style="padding: 10px 15px; border-bottom: 1px solid #21262d;">Читает сообщения из чата Twitch голосом на русском языке</td></tr>
    <tr><td style="padding: 10px 15px; border-bottom: 1px solid #21262d;">🎭 <strong>Разные голоса для ролей</strong></td><td style="padding: 10px 15px; border-bottom: 1px solid #21262d;">Отдельные голоса для модераторов, подписчиков, VIP, стримера и обычных зрителей</td></tr>
    <tr><td style="padding: 10px 15px; border-bottom: 1px solid #21262d;">🎚️ <strong>Выбор голосов через веб-интерфейс</strong></td><td style="padding: 10px 15px; border-bottom: 1px solid #21262d;">Легко меняйте модели из выпадающих списков</td></tr>
    <tr><td style="padding: 10px 15px; border-bottom: 1px solid #21262d;">🤫 <strong>Режим тишины</strong></td><td style="padding: 10px 15px; border-bottom: 1px solid #21262d;">Программа ждёт, пока вы замолкнете, чтобы не перекрывать ваш голос</td></tr>
    <tr><td style="padding: 10px 15px; border-bottom: 1px solid #21262d;">🛑 <strong>Экстренная остановка</strong></td><td style="padding: 10px 15px; border-bottom: 1px solid #21262d;">Горячая клавиша <code style="background: #161b22; padding: 0 4px; border-radius: 4px;">Ctrl+Shift+E</code> — мгновенно прерывает воспроизведение и очищает очередь</td></tr>
    <tr><td style="padding: 10px 15px; border-bottom: 1px solid #21262d;">🌐 <strong>Веб-интерфейс настроек</strong></td><td style="padding: 10px 15px; border-bottom: 1px solid #21262d;">Все настройки доступны через браузер (<a href="http://127.0.0.1:5000" style="color: #58a6ff; text-decoration: none;">http://127.0.0.1:5000</a>)</td></tr>
    <tr><td style="padding: 10px 15px; border-bottom: 1px solid #21262d;">📦 <strong>Портативность</strong></td><td style="padding: 10px 15px; border-bottom: 1px solid #21262d;">Не требует установки — работает из одной папки</td></tr>
    <tr><td style="padding: 10px 15px; border-bottom: 1px solid #21262d;">⚡ <strong>Автоустановка</strong></td><td style="padding: 10px 15px; border-bottom: 1px solid #21262d;"><code style="background: #161b22; padding: 0 4px; border-radius: 4px;">setup.bat</code> скачивает и настраивает всё автоматически</td></tr>
    <tr><td style="padding: 10px 15px; border-bottom: 1px solid #21262d;">🧹 <strong>Фильтрация сообщений</strong></td><td style="padding: 10px 15px; border-bottom: 1px solid #21262d;">Убирает ссылки, команды, упоминания и эмодзи</td></tr>
    <tr><td style="padding: 10px 15px;">⏳ <strong>Умная очередь</strong></td><td style="padding: 10px 15px;">Задержка 5–15 секунд при флуде — не перегружает процессор</td></tr>
  </tbody>
</table>

<hr style="border: none; border-top: 1px solid #30363d; margin: 30px 0;">

<h2 id="%EF%B8%8F-системные-требования" style="color: #f0f6fc; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif; font-weight: 500; font-size: 1.8em;">
  🖥️ Системные требования
</h2>

<ul style="color: #c9d1d9; font-size: 1.05em; line-height: 1.8; padding-left: 20px;">
  <li><strong style="color: #f0f6fc;">Windows 7 / 8 / 10 / 11 (64-bit)</strong></li>
  <li><strong style="color: #f0f6fc;">Микрофон</strong> (для режима тишины, опционально)</li>
  <li><strong style="color: #f0f6fc;">Подключение к интернету</strong> (только для первоначальной установки и подключения к Twitch)</li>
  <li><strong style="color: #f0f6fc;">Около 200 МБ</strong> свободного места</li>
</ul>

<hr style="border: none; border-top: 1px solid #30363d; margin: 30px 0;">

<h2 id="-быстрый-старт" style="color: #f0f6fc; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif; font-weight: 500; font-size: 1.8em;">
  🚀 Быстрый старт
</h2>

<h3 style="color: #f0f6fc; font-weight: 500; font-size: 1.3em;">1️⃣ Клонируйте или скачайте репозиторий</h3>

<pre style="background: #0d1117; padding: 15px; border-radius: 6px; color: #c9d1d9; font-family: 'Consolas', 'Courier New', monospace; font-size: 14px; overflow-x: auto; border: 1px solid #30363d;">
git clone https://github.com/lanarphoenixiik/StreamTTS.git
</pre>
<p style="color: #c9d1d9; margin-top: 5px;">или скачайте ZIP и распакуйте.</p>

<h3 style="color: #f0f6fc; font-weight: 500; font-size: 1.3em;">2️⃣ Запустите установку</h3>

<p style="color: #c9d1d9;"><strong style="color: #f0f6fc;">Дважды кликните по <code style="background: #161b22; padding: 2px 6px; border-radius: 4px;">setup.bat</code></strong>. Он автоматически:</p>
<ul style="color: #c9d1d9; line-height: 1.8;">
  <li>Загрузит портативный Python 3.10</li>
  <li>Установит pip и необходимые библиотеки</li>
  <li>Скачает и настроит <strong style="color: #f0f6fc;">Piper TTS</strong></li>
  <li>Загрузит 4 русские голосовые модели: <strong style="color: #f0f6fc;">Ирина, Денис, Дмитрий, Руслан</strong></li>
</ul>
<p style="color: #8b949e; font-size: 0.9em;">⏳ <strong>Время установки:</strong> ~5–10 минут (зависит от интернета).</p>

<h3 style="color: #f0f6fc; font-weight: 500; font-size: 1.3em;">3️⃣ Настройте токен и канал</h3>

<p style="color: #c9d1d9;">Откройте файл <code style="background: #161b22; padding: 2px 6px; border-radius: 4px;">config.json</code> в корневой папке. Замените:</p>

<pre style="background: #0d1117; padding: 15px; border-radius: 6px; color: #c9d1d9; font-family: 'Consolas', 'Courier New', monospace; font-size: 14px; overflow-x: auto; border: 1px solid #30363d;">
"twitch_token": "oauth:ваш_токен",
"twitch_nick": "имя_бота",
"twitch_channel": "имя_канала"
</pre>

<p style="color: #c9d1d9;">Токен получите на <a href="https://twitchtokengenerator.com/" style="color: #58a6ff; text-decoration: none;">twitchtokengenerator.com</a>, выбрав права <code style="background: #161b22; padding: 0 4px; border-radius: 4px;">chat:read</code> и <code style="background: #161b22; padding: 0 4px; border-radius: 4px;">chat:edit</code>.</p>

<h3 style="color: #f0f6fc; font-weight: 500; font-size: 1.3em;">4️⃣ Запустите приложение</h3>

<p style="color: #c9d1d9;"><strong style="color: #f0f6fc;">Дважды кликните по <code style="background: #161b22; padding: 2px 6px; border-radius: 4px;">start.bat</code></strong>. Откроется консоль и автоматически браузер с веб-интерфейсом.</p>
<p style="color: #c9d1d9;">Если браузер не открылся — перейдите вручную: <a href="http://127.0.0.1:5000" style="color: #58a6ff; text-decoration: none;">http://127.0.0.1:5000</a></p>

<h4 style="color: #f0f6fc; font-weight: 500; font-size: 1.1em;">🖥️ Что вы увидите в консоли</h4>

<table style="width: 100%; border-collapse: collapse; background: #0d1117; border-radius: 8px; overflow: hidden; border: 1px solid #30363d;">
  <tr>
    <td style="padding: 15px; font-family: 'Consolas', 'Courier New', monospace; font-size: 13px; color: #c9d1d9; line-height: 1.8;">
      <span style="color: #58a6ff;">✅</span> Микрофон слушается (режим тишины включён).<br>
      <span style="color: #58a6ff;">✅</span> Бот <span style="color: #f0883e;">lanarphoenixik</span> подключен к каналу <span style="color: #f0883e;">LanarPhoenixik</span><br>
      <span style="color: #8b949e;">📩 В очереди (1): Привет, стример!</span><br>
      <span style="color: #58a6ff;">✅</span> Файл создан, размер: 37536 байт<br>
      <span style="color: #58a6ff;">▶️</span> Воспроизведение началось. Нажмите Ctrl+Shift+E для экстренной остановки.<br>
      <span style="color: #58a6ff;">✅</span> Воспроизведение завершено
    </td>
  </tr>
</table>

<p style="color: #c9d1d9; margin-top: 10px;">Теперь сообщения из чата будут озвучиваться! 🎙️</p>

<hr style="border: none; border-top: 1px solid #30363d; margin: 30px 0;">

<h2 id="%EF%B8%8F-веб-интерфейс" style="color: #f0f6fc; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif; font-weight: 500; font-size: 1.8em;">
  🎛️ Веб-интерфейс
</h2>

<p style="color: #c9d1d9;">В браузере по адресу <a href="http://127.0.0.1:5000" style="color: #58a6ff; text-decoration: none;">http://127.0.0.1:5000</a> доступны настройки:</p>

<ul style="color: #c9d1d9; line-height: 1.8;">
  <li><strong style="color: #f0f6fc;">Twitch</strong> — токен, ник бота, канал</li>
  <li><strong style="color: #f0f6fc;">Piper TTS</strong> — путь к <code style="background: #161b22; padding: 0 4px; border-radius: 4px;">piper.exe</code>, голос по умолчанию, скорость речи</li>
  <li><strong style="color: #f0f6fc;">Голоса для ролей</strong> — выберите модель для модератора, подписчика, VIP и стримера из выпадающего списка</li>
  <li><strong style="color: #f0f6fc;">Микрофон</strong> — включение/отключение режима тишины, порог чувствительности, задержка</li>
  <li><strong style="color: #f0f6fc;">Фильтры</strong> — список игнорируемых ботов, максимальная длина сообщения, размер очереди</li>
</ul>

<p style="color: #c9d1d9;">После изменения настроек нажмите <strong style="color: #f0f6fc;">«Сохранить и перезагрузить»</strong> — изменения применятся без перезапуска.</p>

<hr style="border: none; border-top: 1px solid #30363d; margin: 30px 0;">

<h2 id="-голосовые-модели" style="color: #f0f6fc; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif; font-weight: 500; font-size: 1.8em;">
  🎭 Голосовые модели
</h2>

<p style="color: #c9d1d9;">В комплекте идут 4 модели. Вы можете назначить их для разных ролей:</p>

<table style="width: 100%; border-collapse: collapse; background: #0d1117; border-radius: 8px; overflow: hidden; color: #c9d1d9; font-size: 0.95em;">
  <thead>
    <tr style="background: #161b22;">
      <th style="padding: 12px 15px; text-align: left; border-bottom: 1px solid #30363d;">Имя в интерфейсе</th>
      <th style="padding: 12px 15px; text-align: left; border-bottom: 1px solid #30363d;">Файл</th>
      <th style="padding: 12px 15px; text-align: left; border-bottom: 1px solid #30363d;">Описание</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="padding: 10px 15px; border-bottom: 1px solid #21262d;"><strong>Ирина (женский)</strong></td><td style="padding: 10px 15px; border-bottom: 1px solid #21262d;"><code style="background: #161b22; padding: 0 4px; border-radius: 4px;">ru_RU-irina-medium.onnx</code></td><td style="padding: 10px 15px; border-bottom: 1px solid #21262d;">Голос по умолчанию</td></tr>
    <tr><td style="padding: 10px 15px; border-bottom: 1px solid #21262d;"><strong>Денис (мужской)</strong></td><td style="padding: 10px 15px; border-bottom: 1px solid #21262d;"><code style="background: #161b22; padding: 0 4px; border-radius: 4px;">ru_RU-denis-medium.onnx</code></td><td style="padding: 10px 15px; border-bottom: 1px solid #21262d;">Назначается модераторам</td></tr>
    <tr><td style="padding: 10px 15px; border-bottom: 1px solid #21262d;"><strong>Дмитрий (мужской)</strong></td><td style="padding: 10px 15px; border-bottom: 1px solid #21262d;"><code style="background: #161b22; padding: 0 4px; border-radius: 4px;">ru_RU-dmitri-medium.onnx</code></td><td style="padding: 10px 15px; border-bottom: 1px solid #21262d;">Назначается стримеру</td></tr>
    <tr><td style="padding: 10px 15px;"><strong>Руслан (мужской)</strong></td><td style="padding: 10px 15px;"><code style="background: #161b22; padding: 0 4px; border-radius: 4px;">ru_RU-ruslan-medium.onnx</code></td><td style="padding: 10px 15px;">Назначается VIP</td></tr>
  </tbody>
</table>

<p style="color: #c9d1d9; margin-top: 10px;">Вы можете легко изменить эти назначения через веб-интерфейс.</p>

<hr style="border: none; border-top: 1px solid #30363d; margin: 30px 0;">

<h2 id="%EF%B8%8F-горячие-клавиши" style="color: #f0f6fc; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif; font-weight: 500; font-size: 1.8em;">
  ⌨️ Горячие клавиши
</h2>

<table style="width: 100%; border-collapse: collapse; background: #0d1117; border-radius: 8px; overflow: hidden; color: #c9d1d9; font-size: 0.95em;">
  <thead>
    <tr style="background: #161b22;">
      <th style="padding: 12px 15px; text-align: left; border-bottom: 1px solid #30363d; width: 35%;">Комбинация</th>
      <th style="padding: 12px 15px; text-align: left; border-bottom: 1px solid #30363d; width: 65%;">Действие</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="padding: 10px 15px; border-bottom: 1px solid #21262d; white-space: nowrap;">
        <kbd style="background: #161b22; color: #c9d1d9; border: 1px solid #30363d; border-radius: 4px; padding: 2px 8px; font-family: 'Consolas', monospace; font-size: 0.9em;">Ctrl</kbd>
        +
        <kbd style="background: #161b22; color: #c9d1d9; border: 1px solid #30363d; border-radius: 4px; padding: 2px 8px; font-family: 'Consolas', monospace; font-size: 0.9em;">Shift</kbd>
        +
        <kbd style="background: #161b22; color: #c9d1d9; border: 1px solid #30363d; border-radius: 4px; padding: 2px 8px; font-family: 'Consolas', monospace; font-size: 0.9em;">M</kbd>
      </td>
      <td style="padding: 10px 15px; border-bottom: 1px solid #21262d;">Включить/выключить озвучку (мьют)</td>
    </tr>
    <tr>
      <td style="padding: 10px 15px; white-space: nowrap;">
        <kbd style="background: #161b22; color: #c9d1d9; border: 1px solid #30363d; border-radius: 4px; padding: 2px 8px; font-family: 'Consolas', monospace; font-size: 0.9em;">Ctrl</kbd>
        +
        <kbd style="background: #161b22; color: #c9d1d9; border: 1px solid #30363d; border-radius: 4px; padding: 2px 8px; font-family: 'Consolas', monospace; font-size: 0.9em;">Shift</kbd>
        +
        <kbd style="background: #161b22; color: #c9d1d9; border: 1px solid #30363d; border-radius: 4px; padding: 2px 8px; font-family: 'Consolas', monospace; font-size: 0.9em;">E</kbd>
      </td>
      <td style="padding: 10px 15px;">🛑 <strong style="color: #f0f6fc;">Экстренная остановка</strong> — прерывает текущее воспроизведение, очищает очередь, удаляет временный файл</td>
    </tr>
  </tbody>
</table>

<blockquote style="background: #0d1117; border-left: 4px solid #f0883e; padding: 10px 20px; border-radius: 4px; color: #c9d1d9; margin-top: 15px;">
  <strong style="color: #f0f6fc;">Важно:</strong> Горячие клавиши работают только когда окно консоли находится в фокусе.
</blockquote>

<hr style="border: none; border-top: 1px solid #30363d; margin: 30px 0;">

<h2 id="%EF%B8%8F-конфигурация" style="color: #f0f6fc; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif; font-weight: 500; font-size: 1.8em;">
  ⚙️ Конфигурация
</h2>

<p style="color: #c9d1d9;">Все настройки хранятся в <code style="background: #161b22; padding: 2px 6px; border-radius: 4px;">config.json</code> в корневой папке. Вот полный список параметров:</p>

<table style="width: 100%; border-collapse: collapse; background: #0d1117; border-radius: 8px; overflow: hidden; color: #c9d1d9; font-size: 0.9em;">
  <thead>
    <tr style="background: #161b22;">
      <th style="padding: 10px 12px; text-align: left; border-bottom: 1px solid #30363d;">Параметр</th>
      <th style="padding: 10px 12px; text-align: left; border-bottom: 1px solid #30363d;">Описание</th>
      <th style="padding: 10px 12px; text-align: left; border-bottom: 1px solid #30363d;">По умолчанию</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="padding: 8px 12px; border-bottom: 1px solid #21262d;"><code style="background: #161b22; padding: 0 4px; border-radius: 4px;">twitch_token</code></td><td style="padding: 8px 12px; border-bottom: 1px solid #21262d;">OAuth-токен для чата</td><td style="padding: 8px 12px; border-bottom: 1px solid #21262d;"><code style="background: #161b22; padding: 0 4px; border-radius: 4px;">"oauth:..."</code></td></tr>
    <tr><td style="padding: 8px 12px; border-bottom: 1px solid #21262d;"><code style="background: #161b22; padding: 0 4px; border-radius: 4px;">twitch_nick</code></td><td style="padding: 8px 12px; border-bottom: 1px solid #21262d;">Имя бота (необязательно)</td><td style="padding: 8px 12px; border-bottom: 1px solid #21262d;"><code style="background: #161b22; padding: 0 4px; border-radius: 4px;">"ваш_бот"</code></td></tr>
    <tr><td style="padding: 8px 12px; border-bottom: 1px solid #21262d;"><code style="background: #161b22; padding: 0 4px; border-radius: 4px;">twitch_channel</code></td><td style="padding: 8px 12px; border-bottom: 1px solid #21262d;">Имя канала (без #)</td><td style="padding: 8px 12px; border-bottom: 1px solid #21262d;"><code style="background: #161b22; padding: 0 4px; border-radius: 4px;">"ваш_канал"</code></td></tr>
    <tr><td style="padding: 8px 12px; border-bottom: 1px solid #21262d;"><code style="background: #161b22; padding: 0 4px; border-radius: 4px;">piper_exe</code></td><td style="padding: 8px 12px; border-bottom: 1px solid #21262d;">Путь к <code style="background: #161b22; padding: 0 4px; border-radius: 4px;">piper.exe</code></td><td style="padding: 8px 12px; border-bottom: 1px solid #21262d;"><code style="background: #161b22; padding: 0 4px; border-radius: 4px;">"piper/piper.exe"</code></td></tr>
    <tr><td style="padding: 8px 12px; border-bottom: 1px solid #21262d;"><code style="background: #161b22; padding: 0 4px; border-radius: 4px;">default_model</code></td><td style="padding: 8px 12px; border-bottom: 1px solid #21262d;">Голос по умолчанию</td><td style="padding: 8px 12px; border-bottom: 1px solid #21262d;"><code style="background: #161b22; padding: 0 4px; border-radius: 4px;">"voices/ru_RU-irina-medium.onnx"</code></td></tr>
    <tr><td style="padding: 8px 12px; border-bottom: 1px solid #21262d;"><code style="background: #161b22; padding: 0 4px; border-radius: 4px;">role_models</code></td><td style="padding: 8px 12px; border-bottom: 1px solid #21262d;">Голоса для ролей</td><td style="padding: 8px 12px; border-bottom: 1px solid #21262d;">(указаны выше)</td></tr>
    <tr><td style="padding: 8px 12px; border-bottom: 1px solid #21262d;"><code style="background: #161b22; padding: 0 4px; border-radius: 4px;">mic_device_id</code></td><td style="padding: 8px 12px; border-bottom: 1px solid #21262d;">ID микрофона (null=авто)</td><td style="padding: 8px 12px; border-bottom: 1px solid #21262d;"><code style="background: #161b22; padding: 0 4px; border-radius: 4px;">null</code></td></tr>
    <tr><td style="padding: 8px 12px; border-bottom: 1px solid #21262d;"><code style="background: #161b22; padding: 0 4px; border-radius: 4px;">rms_threshold</code></td><td style="padding: 8px 12px; border-bottom: 1px solid #21262d;">Чувствительность микрофона</td><td style="padding: 8px 12px; border-bottom: 1px solid #21262d;"><code style="background: #161b22; padding: 0 4px; border-radius: 4px;">0.015</code></td></tr>
    <tr><td style="padding: 8px 12px; border-bottom: 1px solid #21262d;"><code style="background: #161b22; padding: 0 4px; border-radius: 4px;">silence_delay</code></td><td style="padding: 8px 12px; border-bottom: 1px solid #21262d;">Задержка перед озвучкой (сек)</td><td style="padding: 8px 12px; border-bottom: 1px solid #21262d;"><code style="background: #161b22; padding: 0 4px; border-radius: 4px;">0.5</code></td></tr>
    <tr><td style="padding: 8px 12px; border-bottom: 1px solid #21262d;"><code style="background: #161b22; padding: 0 4px; border-radius: 4px;">silence_enabled</code></td><td style="padding: 8px 12px; border-bottom: 1px solid #21262d;">Включить режим тишины</td><td style="padding: 8px 12px; border-bottom: 1px solid #21262d;"><code style="background: #161b22; padding: 0 4px; border-radius: 4px;">true</code></td></tr>
    <tr><td style="padding: 8px 12px; border-bottom: 1px solid #21262d;"><code style="background: #161b22; padding: 0 4px; border-radius: 4px;">speech_speed</code></td><td style="padding: 8px 12px; border-bottom: 1px solid #21262d;">Скорость речи (0.5–2.0)</td><td style="padding: 8px 12px; border-bottom: 1px solid #21262d;"><code style="background: #161b22; padding: 0 4px; border-radius: 4px;">0.8</code></td></tr>
    <tr><td style="padding: 8px 12px; border-bottom: 1px solid #21262d;"><code style="background: #161b22; padding: 0 4px; border-radius: 4px;">ignored_users</code></td><td style="padding: 8px 12px; border-bottom: 1px solid #21262d;">Игнорируемые боты</td><td style="padding: 8px 12px; border-bottom: 1px solid #21262d;"><code style="background: #161b22; padding: 0 4px; border-radius: 4px;">["streamelements", ...]</code></td></tr>
    <tr><td style="padding: 8px 12px; border-bottom: 1px solid #21262d;"><code style="background: #161b22; padding: 0 4px; border-radius: 4px;">max_queue_size</code></td><td style="padding: 8px 12px; border-bottom: 1px solid #21262d;">Максимальный размер очереди</td><td style="padding: 8px 12px; border-bottom: 1px solid #21262d;"><code style="background: #161b22; padding: 0 4px; border-radius: 4px;">15</code></td></tr>
    <tr><td style="padding: 8px 12px; border-bottom: 1px solid #21262d;"><code style="background: #161b22; padding: 0 4px; border-radius: 4px;">message_max_len</code></td><td style="padding: 8px 12px; border-bottom: 1px solid #21262d;">Максимальная длина текста</td><td style="padding: 8px 12px; border-bottom: 1px solid #21262d;"><code style="background: #161b22; padding: 0 4px; border-radius: 4px;">150</code></td></tr>
    <tr><td style="padding: 8px 12px;"><code style="background: #161b22; padding: 0 4px; border-radius: 4px;">mute_hotkey</code></td><td style="padding: 8px 12px;">Горячая клавиша для мьюта</td><td style="padding: 8px 12px;"><code style="background: #161b22; padding: 0 4px; border-radius: 4px;">"ctrl+shift+m"</code></td></tr>
  </tbody>
</table>

<hr style="border: none; border-top: 1px solid #30363d; margin: 30px 0;">

<h2 id="-устранение-проблем" style="color: #f0f6fc; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif; font-weight: 500; font-size: 1.8em;">
  🧠 Устранение проблем
</h2>

<table style="width: 100%; border-collapse: collapse; background: #0d1117; border-radius: 8px; overflow: hidden; color: #c9d1d9; font-size: 0.95em;">
  <thead>
    <tr style="background: #161b22;">
      <th style="padding: 12px 15px; text-align: left; border-bottom: 1px solid #30363d;">Проблема</th>
      <th style="padding: 12px 15px; text-align: left; border-bottom: 1px solid #30363d;">Решение</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="padding: 10px 15px; border-bottom: 1px solid #21262d;">❌ <strong style="color: #f0f6fc;">Ошибка аутентификации Twitch</strong></td><td style="padding: 10px 15px; border-bottom: 1px solid #21262d;">Токен истёк или не имеет прав. Сгенерируйте новый на <a href="https://twitchtokengenerator.com/" style="color: #58a6ff; text-decoration: none;">twitchtokengenerator.com</a> с правами <code style="background: #161b22; padding: 0 4px; border-radius: 4px;">chat:read</code> и <code style="background: #161b22; padding: 0 4px; border-radius: 4px;">chat:edit</code>.</td></tr>
    <tr><td style="padding: 10px 15px; border-bottom: 1px solid #21262d;">❌ <strong style="color: #f0f6fc;">Piper завершается с ошибкой (код 3221226505)</strong></td><td style="padding: 10px 15px; border-bottom: 1px solid #21262d;">Несовместимость версий. Удалите папку <code style="background: #161b22; padding: 0 4px; border-radius: 4px;">piper</code>, перезапустите <code style="background: #161b22; padding: 0 4px; border-radius: 4px;">setup.bat</code> для обновления Piper.</td></tr>
    <tr><td style="padding: 10px 15px; border-bottom: 1px solid #21262d;">❌ <strong style="color: #f0f6fc;">Нет звука</strong></td><td style="padding: 10px 15px; border-bottom: 1px solid #21262d;">Проверьте пути к моделям, выберите правильное устройство вывода в Windows. Если Bluetooth-гарнитура — отключите режим «Hands-Free».</td></tr>
    <tr><td style="padding: 10px 15px; border-bottom: 1px solid #21262d;">❌ <strong style="color: #f0f6fc;">Бот не видит сообщения</strong></td><td style="padding: 10px 15px; border-bottom: 1px solid #21262d;">Проверьте регистр имени канала, пишите с другого аккаунта (бот игнорирует свои сообщения).</td></tr>
    <tr><td style="padding: 10px 15px; border-bottom: 1px solid #21262d;">❌ <strong style="color: #f0f6fc;">Веб-интерфейс не открывается</strong></td><td style="padding: 10px 15px; border-bottom: 1px solid #21262d;">Проверьте, не занят ли порт 5000. Откройте вручную <a href="http://127.0.0.1:5000" style="color: #58a6ff; text-decoration: none;">http://127.0.0.1:5000</a>.</td></tr>
    <tr><td style="padding: 10px 15px;">❌ <strong style="color: #f0f6fc;">Режим тишины не работает</strong></td><td style="padding: 10px 15px;">Укажите ID микрофона вручную через веб-интерфейс. Отрегулируйте порог <code style="background: #161b22; padding: 0 4px; border-radius: 4px;">rms_threshold</code>.</td></tr>
  </tbody>
</table>

<hr style="border: none; border-top: 1px solid #30363d; margin: 30px 0;">

<h2 id="-структура-проекта" style="color: #f0f6fc; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif; font-weight: 500; font-size: 1.8em;">
  📁 Структура проекта
</h2>

<div style="background: #0d1117; border-radius: 8px; border: 1px solid #30363d; padding: 15px 20px; font-family: 'Consolas', 'Courier New', monospace; font-size: 14px; color: #c9d1d9; overflow-x: auto;">
<pre style="margin: 0; padding: 0; line-height: 1.7;">
📁 StreamTTS/
├── 📁 app/
│   ├── 📄 main.py               <span style="color: #8b949e;"># Основной код</span>
│   ├── 📄 config.py             <span style="color: #8b949e;"># Работа с конфигом</span>
│   ├── 📄 web_ui.py             <span style="color: #8b949e;"># Веб-сервер настроек</span>
│   └── 📁 templates/
│       └── 📄 settings.html     <span style="color: #8b949e;"># HTML-шаблон</span>
├── 📄 .gitignore                <span style="color: #8b949e;"># Игнорируемые файлы</span>
├── 📄 README.md                 <span style="color: #8b949e;"># Этот файл</span>
├── 📄 setup.bat                 <span style="color: #8b949e;"># Запуск установки</span>
├── 📄 setup.ps1                 <span style="color: #8b949e;"># PowerShell-скрипт установки</span>
├── 📄 start.bat                 <span style="color: #8b949e;"># Запуск приложения</span>
└── 📄 config.json               <span style="color: #8b949e;"># Файл настроек (создаётся автоматически)</span>
</pre>
</div>

<blockquote style="background: #0d1117; border-left: 4px solid #8b949e; padding: 10px 20px; border-radius: 4px; color: #c9d1d9;">
  📌 Папки <code style="background: #161b22; padding: 0 4px; border-radius: 4px;">python/</code>, <code style="background: #161b22; padding: 0 4px; border-radius: 4px;">piper/</code>, <code style="background: #161b22; padding: 0 4px; border-radius: 4px;">voices/</code> создаются во время установки и не хранятся в репозитории.
</blockquote>

<hr style="border: none; border-top: 1px solid #30363d; margin: 30px 0;">

<h2 id="-лицензия" style="color: #f0f6fc; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif; font-weight: 500; font-size: 1.8em;">
  📜 Лицензия
</h2>

<p style="color: #c9d1d9;">Проект распространяется под лицензией <strong style="color: #f0f6fc;">MIT</strong>. Вы можете свободно использовать, изменять и распространять его с указанием авторства.</p>

<hr style="border: none; border-top: 1px solid #30363d; margin: 30px 0;">

<p align="center" style="color: #c9d1d9; font-size: 1.2em; font-weight: 500;">
  🎥🎙️🔥 <strong style="color: #f0f6fc;">Приятных стримов!</strong>
</p>
