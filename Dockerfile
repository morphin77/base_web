FROM python:3.12.5-slim

# Устанавливаем Poetry
RUN pip install poetry

# Отключаем создание виртуального окружения (будем использовать системный Python)
ENV POETRY_VIRTUALENVS_CREATE=false

WORKDIR /app

COPY pyproject.toml /app/pyproject.toml
#добавить poetry.lock

RUN poetry install --no-root

COPY . /app

CMD ["poetry", "run", "app"]
