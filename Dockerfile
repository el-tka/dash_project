# Базовый образ с Python
FROM python:3.9-slim

# Устанавливаем необходимые зависимости
RUN apt-get update && apt-get install -y \
    curl \
    apt-transport-https \
    unixodbc-dev \
    gcc \
    gpg \
    g++

# Скачиваем и устанавливаем драйвер ODBC для MS SQL с помощью GPG
RUN curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > microsoft.gpg && \
    mv microsoft.gpg /etc/apt/trusted.gpg.d/microsoft.gpg && \
    curl https://packages.microsoft.com/config/ubuntu/20.04/prod.list > /etc/apt/sources.list.d/mssql-release.list && \
    apt-get update && ACCEPT_EULA=Y apt-get install -y msodbcsql17

# Устанавливаем pip и обновляем его
RUN python -m pip install --upgrade pip

# Создаем директорию для проекта
WORKDIR /app

# Копируем файлы проекта в контейнер
COPY . /app

# Устанавливаем зависимости через requirements.txt
RUN pip install -r requirements.txt

# Открываем порт 8050 для Dash приложения
EXPOSE 8050

# Команда для запуска Dash приложения
CMD ["python", "app_styled.py"]
