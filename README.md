﻿# AnyStart - Программа для запуска приложений при загрузке Windows

## Описание
AnyStart - это программа на Python, которая позволяет добавлять любые приложения или файлы для автоматического запуска при старте Windows. Программа использует только встроенные библиотеки Python: `tkinter`, `json` и `os`.

## Известная проблема
**Есть проблема с кодировкой, поэтому при запуске bat файла может некорректно указываться путь**

## Особенности
- Простой графический интерфейс
- Сохранение списка программ между сеансами
- Автоматическое создание bat-файла в папке автозагрузки Windows
- Не требует установки дополнительных зависимостей

## Установка и запуск
Программу можно запустить двумя способами:
1. Использовать готовый исполняемый файл `app_gui.exe` из папки `output` (не требует установки Python)
2. Запустить исходный код `app_gui.py` напрямую (требуется Python 3.x)

## Использование
1. Нажмите "Add file" для добавления файла/приложения
2. Выберите нужный файл в диалоговом окне
3. Нажмите "Save config" для сохранения изменений
4. Чтобы удалить файл, выделите его в списке и нажмите "Delete file"

## Технические детали
- Конфигурация сохраняется в `%APPDATA%\pet_app_config.json`
- Скрипт автозагрузки создается в папке автозагрузки Windows как `easy_start.bat`

---

# AnyStart - Program to Run Applications on Windows Startup

## Description
AnyStart is a Python program that allows you to add any applications or files to be launched automatically when Windows starts. The program uses only built-in Python libraries: `tkinter`, `json`, and `os`.

## Features
- Simple GUI interface
- Saves program list between sessions
- Automatically creates a bat-file in Windows startup folder
- No additional dependencies required

## Installation and Launch
You can run the program in two ways:
1. Use the ready-made executable `app_gui.exe` from the `output` folder (doesn't require Python installation)
2. Run the source code `app_gui.py` directly (requires Python 3.x)

## Usage
1. Click "Add file" to add a file/application
2. Select the desired file in the dialog window
3. Click "Save config" to save changes
4. To remove a file, select it in the list and click "Delete file"

## Technical Details
- Configuration is saved to `%APPDATA%\pet_app_config.json`
- The startup script is created in Windows startup folder as `easy_start.bat`
