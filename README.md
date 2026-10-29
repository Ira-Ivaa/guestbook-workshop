# guestbook

Гостевая книга на FastAPI: можно оставить сообщение и посмотреть все оставленные.
Данные хранятся в PostgreSQL.

## Эндпоинты

- `GET /` — приветствие
- `GET /health` — проверка, жив ли сервис
- `GET /messages` — список сообщений (новые сверху)
- `POST /messages` — добавить сообщение: `{"author": "...", "text": "..."}`

## Запуск

    cp .env.example .env      # задать свой пароль в POSTGRES_PASSWORD
    docker compose up -d
    curl http://localhost:8000/health

## Разработка

    uv sync
    uv run ruff check .
    uv run pytest

## CI/CD

- каждый пуш: линтер и тесты
- пуш в `main`: образ `ghcr.io/ira-ivaa/guestbook-workshop:latest`
- git-тег `vX.Y.Z`: образ `ghcr.io/ira-ivaa/guestbook-workshop:X.Y.Z`

## Релиз

    git tag -a v1.2.0 -m "v1.2.0"
    git push origin v1.2.0

Изменения описываются в [CHANGELOG.md](CHANGELOG.md).

## Если что-то сломалось

См. [RUNBOOK.md](RUNBOOK.md).
