FROM python:3.10

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONPATH=/app/store

RUN pip install poetry==1.3.2 && poetry config virtualenvs.create false

WORKDIR /store

COPY pyproject.toml .
COPY poetry.lock .
RUN poetry install
COPY . .

RUN rm -r nginx
RUN python manage.py collectstatic --no-input

EXPOSE 8000