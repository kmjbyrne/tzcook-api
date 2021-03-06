import logging
from logging.handlers import RotatingFileHandler

DEFAULT_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'


def get_rotating_file_handler(logfile='/tmp/app.log', level=logging.INFO, log_format=DEFAULT_FORMAT):
    log_file_handler = RotatingFileHandler(logfile)
    log_file_handler.setLevel(level)
    log_file_handler.setFormatter(logging.Formatter(log_format))
    return log_file_handler


def getlogger():
    logger = logging.getLogger(__name__)

    error_logger_file_handler = RotatingFileHandler('/tmp/tzcook.error.log')
    error_logger_file_handler.setLevel(logging.ERROR)
    log_format = logging.Formatter(DEFAULT_FORMAT)
    error_logger_file_handler.setFormatter(log_format)

    info_logger_file_handler = RotatingFileHandler('/tmp/tzcook.info.log')
    info_logger_file_handler.setLevel(logging.INFO)
    log_format = logging.Formatter(DEFAULT_FORMAT)
    info_logger_file_handler.setFormatter(log_format)

    logger.addHandler(info_logger_file_handler)
    logger.addHandler(error_logger_file_handler)
    logger.setLevel(logging.INFO)

    return logger
