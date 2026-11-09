# 🐍 hello-python-releases — PyInstaller → GitHub Releases

Учебный CI/CD-проект для Python. GitHub Actions запускает Ruff и pytest при push в `main` и pull request. При push тега версии приложение упаковывается PyInstaller на трёх операционных системах, а готовые исполняемые файлы прикладываются к GitHub Release.

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

PyInstaller запускается на каждой целевой ОС отдельно: бинарные приложения для Windows, macOS и Linux собираются нативными runner-ами.

## Как создать Release

```bash
git tag v1.0.0
git push origin v1.0.0
```

Сначала workflow запускает тесты и линтер. После успешного завершения матрица собирает исполняемые файлы, а job `release` публикует их в GitHub Releases.

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

## Permissions

Для CI используется `contents: read`. Job публикации получает `contents: write` и создаёт релиз с помощью встроенного `GITHUB_TOKEN`.

[Главный каталог CI/CD проектов](https://github.com/anitouchq/CI-CD-Pipelines)
