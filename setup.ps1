# setup.ps1
$ErrorActionPreference = "Continue"

$root = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $root

chcp 65001 | Out-Null

Write-Host "Установка StreamTTS Portable..." -ForegroundColor Cyan
Write-Host ""
Write-Host "Это займет некоторое время, так как будут скачаны Python, Piper и голосовые модели." -ForegroundColor Yellow
Write-Host ""

# --- URLs для скачивания ---
$pythonUrl = "https://www.python.org/ftp/python/3.10.11/python-3.10.11-embed-amd64.zip"
$pipUrl = "https://bootstrap.pypa.io/get-pip.py"
# ПРАВИЛЬНАЯ ССЫЛКА НА PIPER (рабочая)
$piperUrl = "https://github.com/rhasspy/piper/releases/download/2023.11.14-2/piper_windows_amd64.zip"

# --- Список голосовых моделей ---
$models = @(
    @{ name = "irina"; url = "https://huggingface.co/rhasspy/piper-voices/resolve/main/ru/ru_RU/irina/medium/ru_RU-irina-medium.onnx?download=true" },
    @{ name = "denis"; url = "https://huggingface.co/rhasspy/piper-voices/resolve/main/ru/ru_RU/denis/medium/ru_RU-denis-medium.onnx?download=true" },
    @{ name = "dmitri"; url = "https://huggingface.co/rhasspy/piper-voices/resolve/main/ru/ru_RU/dmitri/medium/ru_RU-dmitri-medium.onnx?download=true" },
    @{ name = "ruslan"; url = "https://huggingface.co/rhasspy/piper-voices/resolve/main/ru/ru_RU/ruslan/medium/ru_RU-ruslan-medium.onnx?download=true" }
)

# --- Функция скачивания ---
function Download-File {
    param($url, $dest)
    $maxAttempts = 3
    $attempt = 1
    while ($attempt -le $maxAttempts) {
        try {
            Write-Host "Скачивание: $url" -ForegroundColor Yellow
            Invoke-WebRequest -Uri $url -OutFile $dest -UseBasicParsing
            return $true
        } catch {
            Write-Host "Попытка $attempt не удалась. Ошибка: $($_.Exception.Message)" -ForegroundColor Red
            $attempt++
            if ($attempt -le $maxAttempts) {
                Write-Host "Повтор через 2 секунды..." -ForegroundColor Yellow
                Start-Sleep -Seconds 2
            }
        }
    }
    Write-Host "❌ Не удалось скачать файл: $url" -ForegroundColor Red
    return $false
}

# --- Создание папок ---
$folders = @("python", "piper", "voices", "app")
foreach ($f in $folders) {
    if (-not (Test-Path $f)) {
        New-Item -ItemType Directory -Path $f -Force | Out-Null
    }
}

# --- 1. Python ---
if (-not (Test-Path "python\python.exe")) {
    Write-Host "[1/5] Установка портативного Python..." -ForegroundColor Cyan
    $pythonZip = "python.zip"
    if (Download-File $pythonUrl $pythonZip) {
        Expand-Archive -Path $pythonZip -DestinationPath "python" -Force
        Remove-Item $pythonZip -Force
        Get-ChildItem "python\*._pth" | ForEach-Object {
            $content = Get-Content $_.FullName
            $newContent = $content -replace '#import site', 'import site'
            Set-Content $_.FullName $newContent
        }
    } else {
        Write-Host "❌ Ошибка установки Python." -ForegroundColor Red
        exit 1
    }
} else {
    Write-Host "[1/5] Python уже установлен." -ForegroundColor Green
}

# --- 2. Pip ---
if (-not (Test-Path "python\Lib\site-packages\pip")) {
    Write-Host "[2/5] Установка pip..." -ForegroundColor Cyan
    if (Download-File $pipUrl "get-pip.py") {
        & "python\python.exe" get-pip.py
        Remove-Item "get-pip.py" -Force
    } else {
        Write-Host "❌ Ошибка установки pip." -ForegroundColor Red
        exit 1
    }
} else {
    Write-Host "[2/5] Pip уже установлен." -ForegroundColor Green
}

# --- 3. Библиотеки Python ---
Write-Host "[3/5] Установка Python библиотек..." -ForegroundColor Cyan
& "python\python.exe" -m pip install --upgrade pip
& "python\python.exe" -m pip install twitchio sounddevice numpy keyboard flask pygame

# --- 4. Piper (исправленная ссылка) ---
if (-not (Test-Path "piper\piper.exe")) {
    Write-Host "[4/5] Установка Piper..." -ForegroundColor Cyan
    $piperZip = "piper.zip"
    if (Download-File $piperUrl $piperZip) {
        Expand-Archive -Path $piperZip -DestinationPath "piper_temp" -Force
        $piperExtract = Get-ChildItem "piper_temp" -Directory | Select-Object -First 1
        if ($piperExtract) {
            Move-Item "$($piperExtract.FullName)\*" "piper\" -Force
        } else {
            Move-Item "piper_temp\*" "piper\" -Force
        }
        Remove-Item "piper_temp" -Recurse -Force
        Remove-Item $piperZip -Force
    } else {
        Write-Host "❌ Ошибка установки Piper." -ForegroundColor Red
        exit 1
    }
} else {
    Write-Host "[4/5] Piper уже установлен." -ForegroundColor Green
}

# --- 5. Голосовые модели ---
Write-Host "[5/5] Скачивание голосовых моделей..." -ForegroundColor Cyan
foreach ($model in $models) {
    $modelName = $model.name
    $onnxUrl = $model.url
    $jsonUrl = $onnxUrl -replace '\.onnx\?download=true', '.onnx.json?download=true'
    
    $onnxFile = "voices\ru_RU-$modelName-medium.onnx"
    $jsonFile = "voices\ru_RU-$modelName-medium.onnx.json"
    
    if (-not (Test-Path $onnxFile)) {
        Write-Host "Скачивание модели $modelName..." -ForegroundColor Yellow
        Download-File $onnxUrl $onnxFile
    } else {
        Write-Host "Модель $modelName уже скачана." -ForegroundColor Green
    }
    
    if (-not (Test-Path $jsonFile)) {
        Download-File $jsonUrl $jsonFile
    } else {
        Write-Host "Конфиг для $modelName уже скачан." -ForegroundColor Green
    }
}

# --- Создание config.json ---
if (-not (Test-Path "config.json")) {
    Write-Host "Создание файла конфигурации config.json..." -ForegroundColor Cyan
    $config = @"
{
    "twitch_token": "oauth:ваш_токен",
    "twitch_nick": "ваш_бот",
    "twitch_channel": "ваш_канал",
    "piper_exe": "piper/piper.exe",
    "default_model": "voices/ru_RU-irina-medium.onnx",
    "role_models": {
        "moderator": "voices/ru_RU-denis-medium.onnx",
        "subscriber": "voices/ru_RU-irina-medium.onnx",
        "vip": "voices/ru_RU-ruslan-medium.onnx",
        "broadcaster": "voices/ru_RU-dmitri-medium.onnx"
    },
    "mic_device_id": null,
    "rms_threshold": 0.015,
    "silence_delay": 0.5,
    "silence_enabled": true,
    "speech_speed": 0.8,
    "ignored_users": ["streamelements", "nightbot", "fossabot", "moobot"],
    "max_queue_size": 15,
    "message_max_len": 150,
    "mute_hotkey": "ctrl+shift+m"
}
"@
    Set-Content -Path "config.json" -Value $config -Encoding UTF8
}

Write-Host ""
Write-Host "✅ Установка завершена!" -ForegroundColor Green
Write-Host ""
Write-Host "Теперь выполните следующие шаги:" -ForegroundColor Yellow
Write-Host "1. Отредактируйте файл config.json (укажите токен, ник бота, канал)."
Write-Host "2. Запустите start.bat для запуска программы."
Write-Host ""
Read-Host "Нажмите Enter для выхода"