import logging
import sys #нужен чтобы получить доступ к стандартному потоку вывода sys.stdout(куда обычно пишет print())
from pathlib import Path

logger = logging.getLogger("app")
logger.setLevel(logging.DEBUG) #устанавливаем минимальный уровень - DEBUG(DEBUG, INFO, WARNING, ERROR, CRITICAL)

formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
) #формат сообщений: время, имя логгера, уровень, сообщение

#Консольный обработчик
console_handler = logging.StreamHandler(sys.stdout) #StreamHandler - обработчик который направляет логи в поток(stream)
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(formatter)

#Файловый обработчик(запись в файл)
log_file = Path("app.log")
file_handler = logging.FileHandler(log_file, encoding="utf-8")
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

#Регистрация обработчиков
logger.addHandler(console_handler)
logger.addHandler(file_handler)