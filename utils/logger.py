import logging
import sys


def setup_logger(name: str = "app_logger") -> logging.Logger:
    """
    Создает и настраивает логгер для приложения.
    """

    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # если логгер уже настроен — не добавляем handlers повторно
    if logger.hasHandlers():
        return logger

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    # вывод в консоль
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)

    logger.addHandler(console_handler)

    return logger