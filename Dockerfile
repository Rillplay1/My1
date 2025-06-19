# Используем официальный образ от Microsoft с предустановленным Playwright и Python
FROM mcr.microsoft.com/playwright/python:v1.52.0-jammy

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app


# Копируем файл зависимостей в контейнер
COPY requirements.txt .

# Устанавливаем Python-зависимости из requirements.txt без кэширования
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь остальной проект внутрь контейнера
COPY . .

# Устанавливаем необходимые утилиты и Allure CLI:
# - curl, unzip и Java (Allure требует Java)
# - загружаем Allure CLI zip-архив
# - распаковываем его в /opt/
# - создаём символическую ссылку на команду allure в /usr/bin
# - удаляем архив и чистим кеш apt для уменьшения размера образа
RUN apt-get update && apt-get install -y curl unzip openjdk-11-jre-headless \
 && curl -o allure.zip -sSL https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/2.21.0/allure-commandline-2.21.0.zip \
 && unzip allure.zip -d /opt/ \
 && ln -s /opt/allure-2.21.0/bin/allure /usr/bin/allure \
 && rm allure.zip \
 && apt-get clean && rm -rf /var/lib/apt/lists/*

# Команда по умолчанию при запуске контейнера — запуск pytest с генерацией allure-результатов
CMD ["pytest", "--alluredir=allure-results"]
