# logger.py

import logging
import colorlog
from logging.handlers import RotatingFileHandler

# Конфигурация colorlog.ColoredFormatter для консоли
formatter = colorlog.ColoredFormatter(
    '%(asctime)s | %(log_color)s%(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    log_colors={
        'DEBUG': 'white',
        'INFO': 'green',
        'WARNING': 'yellow',
        'ERROR': 'red',
        'CRITICAL': 'bold_red',
    },
    reset=True,
    style='%'
)

# Конфигурация logging.Formatter для файла
file_formatter = logging.Formatter(
    '%(asctime)s | %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# Создание logging.StreamHandler для консоли
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

# Создание  logging.FileHandler для файла
file_handler = RotatingFileHandler('logger.log', maxBytes=1048576, backupCount=5)
file_handler.setFormatter(file_formatter)

# Создание logger
logger = logging.getLogger(__name__)
logger.addHandler(stream_handler)
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)

if __name__ == '__main__':
    logger.debug('Debug message')
    logger.info('Info message')
    logger.warning('Warning message')
    logger.error('Error message')
    logger.critical('Critical message')
