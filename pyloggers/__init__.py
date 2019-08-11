#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# date:        2019/5/26
# author:      he.zhiming
#

from __future__ import (absolute_import, unicode_literals)

import functools
import logging
import sys
import threading
from logging import handlers

_THREADLOCAL = threading.local()
_THREADLOCAL.loggername_logger = {}
DEFAULT_FORMAT = ('[%(levelname)s] '
                  '[%(asctime)s %(created)f] '
                  '[%(name)s %(module)s] '
                  '[%(process)d %(processName)s %(thread)d %(threadName)s] '
                  '[%(filename)s %(lineno)s %(funcName)s] '
                  '%(message)s')
DEFAULT_FORMATTER = logging.Formatter(fmt=DEFAULT_FORMAT)


class _Logger(object):
    _DEFAULT_FORMAT = DEFAULT_FORMAT
    _DEFAULT_FORMATTER = DEFAULT_FORMATTER
    _DEFAULT_LOG_FILENAME = './PYTHON_LOG.log'
    _DEFAULT_SINGLE_FILE_MAX_BYTES = (1 * 1024 * 1024 * 1024)  # 1G
    _DEFAULT_BACKUP_COUNT = 10
    _DEFAULT_FILE_ENCODING = 'UTF-8'

    def __init__(self, logger_name, logger_level=logging.INFO, logger_filename=None, max_bytes=None, backup_count=None):
        self._logger_name = logger_name
        self._logger_filename = logger_filename or self._DEFAULT_LOG_FILENAME
        self._max_bytes = max_bytes or self._DEFAULT_SINGLE_FILE_MAX_BYTES
        self._backup_count = (backup_count or self._DEFAULT_BACKUP_COUNT)

        self._logger = logging.Logger(logger_name, level=logger_level)

        self._init()

    def get_real_logger(self):
        """

        :rtype: logging.Logger
        :return:
        """
        return self._logger

    def _init(self):
        if self._logger_filename is None:
            self._logger.addHandler(self._get_console_stream_handler())
            return
        else:
            self._logger.addHandler(self._get_rotating_file_handler())

    def _get_console_stream_handler(self):
        h = logging.StreamHandler()
        formatter = logging.Formatter(fmt=self._DEFAULT_FORMAT)
        h.setFormatter(formatter)

        return h

    def _get_rotating_file_handler(self):
        h = handlers.RotatingFileHandler(self._logger_filename,
                                         maxBytes=self._max_bytes,
                                         backupCount=self._backup_count,
                                         encoding=self._DEFAULT_FILE_ENCODING)

        h.setFormatter(self._DEFAULT_FORMATTER)

        return h

    @classmethod
    def get_console_logger(cls, logger_name, level=logging.DEBUG):
        logger = logging.Logger(logger_name)
        h = logging.StreamHandler(stream=sys.stdout)
        h.setFormatter(cls._DEFAULT_FORMATTER)
        h.setLevel(level)

        logger.addHandler(h)
        logger.setLevel(level)

        return logger


def make_file_logger(logger_name, level=logging.INFO, filename=None, max_bytes=None, backup_count=None):
    """获取一个logger,记录内容到文件里面

    :param logger_name:
    :param level:
    :param filename:
    :param max_bytes:
    :param backup_count:
    :return:
    """
    if logger_name in _THREADLOCAL.loggername_logger:
        return _THREADLOCAL.loggername_logger[logger_name]

    logger = _Logger(
        logger_name,
        logger_level=level,
        logger_filename=filename,
        max_bytes=max_bytes,
        backup_count=backup_count).get_real_logger()

    _THREADLOCAL.loggername_logger[logger_name] = logger

    return logger


# 记录控制台输入的日志器
CONSOLE = _Logger.get_console_logger('CONSOLE_LOGGER')


def log_input_output(func):
    """记录函数的输入-输出值

    Usage:
        @log
        def add(a, b):

    :param func:
    :return:
    """

    @functools.wraps(func)
    def _wrapper(*args, **kwargs):
        CONSOLE.info("====function start.==== {args}  {kwargs}".format(args=args, kwargs=kwargs))

        func_result = func(*args, **kwargs)

        CONSOLE.info("==== function end. ==== {func_result}".format(func_result=func_result))

        return func_result

    return _wrapper
