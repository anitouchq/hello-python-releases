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

[Главный каталог CI/CD проектов](https://github.com/anitouchq/CI-CD-Pipelines)

## Скриншоты

Добавьте изображения в каталог `screenshots/`:

- `screenshots/application.png` — пример запуска собранного приложения;
- `screenshots/github-actions-release.png` — успешная матричная сборка PyInstaller;
- `screenshots/github-release.png` — опубликованный Release с файлами для ОС.

![Пример работы приложения](screenshots/application.png)
![Сборка GitHub Actions](screenshots/github-actions-release.png)
![Опубликованный GitHub Release](screenshots/github-release.png)

## Как создать Release-сборку

После того как изменения закоммичены в `main`, отправьте тег версии:

```bash
git checkout main
git pull origin main
git tag v1.0.0
git push origin v1.0.0
```

Workflow реагирует на теги вида `v*`. Сначала выполняются Ruff и pytest, затем PyInstaller собирает приложение на Linux, macOS и Windows runner'ах. В конце отдельный job создаёт GitHub Release и прикладывает бинарники.

Для следующих версий используйте новый тег, например `v1.0.1`. Не создавайте повторно уже существующий тег.

- [Проверить GitHub Actions](https://github.com/anitouchq/hello-python-releases/actions)
- [Скачать Release](https://github.com/anitouchq/hello-python-releases/releases)
