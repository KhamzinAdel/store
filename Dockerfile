FROM python:3.10

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN pip install poetry==1.3.2 && poetry config virtualenvs.create false

WORKDIR /store

COPY . .
COPY pyproject.toml .
COPY poetry.lock .
RUN poetry install

EXPOSE 8000