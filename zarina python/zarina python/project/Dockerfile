## Используем Python 3.12 вместо 3.9
#FROM python:3.12-slim
#
## Указываем рабочую директорию внутри контейнера
#WORKDIR /app
#
## Копируем файл с зависимостями в контейнер и переименовываем его в requirements.txt
#COPY requirements.txt /app/requirements.txt
#
## Устанавливаем зависимости
#RUN pip install --no-cache-dir -r /app/requirements.txt
#
## Копируем всё содержимое вашей папки в контейнер
#COPY . /app
#
## Указываем команду для запуска вашего Django-приложения
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]


# Используем Python 3.12 вместо 3.9
FROM python:3.12-slim

# Указываем рабочую директорию внутри контейнера
WORKDIR /app

# Устанавливаем системные зависимости
RUN apt-get update && apt-get install -y \
    libpq-dev gcc && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Копируем файл с зависимостями в контейнер
COPY requirements.txt /app/requirements.txt

# Устанавливаем зависимости Python
RUN pip install --no-cache-dir -r /app/requirements.txt

# Копируем всё содержимое вашей папки в контейнер
COPY . /app

# Указываем команду для запуска вашего Django-приложения
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
