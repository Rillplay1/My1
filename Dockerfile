#FROM mcr.microsoft.com/playwright/python:v1.52.0-jammy
#WORKDIR /app
#COPY requirements.txt .
#RUN pip install --no-cache-dir -r requirements.txt
#COPY . .
#RUN apt-get update && apt-get install -y curl unzip openjdk-11-jre-headless \
# && curl -o allure.zip -sSL https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/2.21.0/allure-commandline-2.21.0.zip \
# && unzip allure.zip -d /opt/ \
# && ln -s /opt/allure-2.21.0/bin/allure /usr/bin/allure \
# && rm allure.zip
#CMD ["pytest", "--alluredir=allure-results"]


FROM mcr.microsoft.com/playwright/python:v1.52.0-jammy

# Установка рабочей директории
WORKDIR /app

# Установка Python-зависимостей
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копирование остального кода
COPY . .

# Установка Allure CLI
RUN apt-get update && apt-get install -y curl unzip openjdk-11-jre-headless \
 && curl -o allure.zip -sSL https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/2.21.0/allure-commandline-2.21.0.zip \
 && unzip allure.zip -d /opt/ \
 && ln -s /opt/allure-2.21.0/bin/allure /usr/bin/allure \
 && rm allure.zip \
 && apt-get clean && rm -rf /var/lib/apt/lists/*

# Команда по умолчанию — запуск тестов с генерацией Allure-результатов
CMD ["pytest", "--alluredir=allure-results"]
