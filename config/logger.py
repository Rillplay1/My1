import logging
import os

# Папка для логов (в корне проекта)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG_DIR = os.path.join(BASE_DIR, 'logs')
os.makedirs(LOG_DIR, exist_ok=True)

# Путь к лог-файлу
LOG_FILE = os.path.join(LOG_DIR, 'test.log')

# Создаем логгер
logger = logging.getLogger("MyLogger")
logger.setLevel(logging.DEBUG)

# Если ещё нет хендлеров — добавляем (чтобы не дублировалось)
if not logger.handlers:
    file_handler = logging.FileHandler(LOG_FILE, mode='a', encoding='utf-8')
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)