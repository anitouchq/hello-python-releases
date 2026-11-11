# hello-python-releases

[![CI](https://github.com/anitouchq/hello-python-releases/actions/workflows/ci.yml/badge.svg)](https://github.com/anitouchq/hello-python-releases/actions)
![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white)

Учебный CI/CD-проект на Python. GitHub Actions запускает Ruff и pytest при push в `main` и pull request. При push тега версии приложение упаковывается PyInstaller на трёх операционных системах и публикуется в GitHub Releases.

## CI checks

- `ruff check .` — статический анализ;
- `ruff format --check .` — проверка форматирования;
- `python -m pytest -v` — модульные тесты.

## Release matrix

| ОС | Файл |
|---|---|
| Linux x64 | `hello-python-linux-x64` |
| macOS | `hello-python-macos` |
| Windows x64 | `hello-python-windows-x64.exe` |

PyInstaller запускается отдельно на каждой целевой ОС: готовые приложения для Windows, macOS и Linux собираются нативными runner'ами.

## Как создать Release

```bash
git tag v1.0.0
git push origin v1.0.0
```

Сначала workflow запускает линтер и тесты. Затем матрица собирает исполняемые файлы, а job `release` публикует их в [GitHub Releases](https://github.com/anitouchq/hello-python-releases/releases).

## Локальный запуск

Рекомендуется Python 3.12:

```bash
python -m pip install ruff pytest pyinstaller
ruff check .
ruff format --check .
python -m pytest -v
python main.py
python -m PyInstaller --onefile --name hello-python main.py
```

## Структура проекта

| Файл или каталог | Назначение |
|---|---|
| `.github/workflows/ci.yml` | Линтинг, тесты, матричная сборка и публикация Release |
| `hello/__init__.py` | Инициализация Python-пакета |
| `hello/greeting.py` | Логика формирования приветствия |
| `main.py` | Точка входа CLI-приложения |
| `tests/test_greeting.py` | Тесты логики приветствия |
| `pyproject.toml` | Метаданные проекта и настройки инструментов |
| `.gitignore` | Локальные файлы, исключаемые из Git |

## Результаты

- [GitHub Actions](https://github.com/anitouchq/hello-python-releases/actions)
- [Опубликованные релизы](https://github.com/anitouchq/hello-python-releases/releases)


## 📸 Скриншоты

**Actions (CI/CD):**

![GitHub Actions — успешная сборка](screenshots/github-actions-release.png)

**Release v1.0.0 (3 бинарника):**

![GitHub Release с файлами для трёх ОС](screenshots/github-release.png)

### Запуск приложения

![Запуск CLI-приложения](screenshots/application.png)

[Главный каталог CI/CD проектов](https://github.com/anitouchq/CI-CD-Pipelines)
