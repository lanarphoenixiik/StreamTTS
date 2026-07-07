@echo off
chcp 65001 >nul
echo Установка StreamTTS Portable...
echo.
echo Это займет некоторое время, так как будут скачаны Python, Piper и голосовая модель.
echo.
powershell -ExecutionPolicy Bypass -File "%~dp0setup.ps1"
pause