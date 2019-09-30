#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# date:        2019/5/26
# author:      he.zhiming
#

from __future__ import (absolute_import, unicode_literals)

import logging
from logging import config

__version__ = '1.0'

DEFAULT_FORMAT = ('[%(levelname)s] '
                  '[%(asctime)s %(created)f] '
                  '[%(name)s %(module)s] '
                  '[%(process)d %(processName)s %(thread)d %(threadName)s] '
                  '[%(filename)s %(lineno)s %(funcName)s] '
                  '%(message)s')
_CONSOLE_LOGGER_NAME = 'console'

config.dictConfig({
    'version': 1,
    'disable_existing_loggers': False,

    'formatters': {
        # 开发环境下的配置(越详细越好, 暴露更多信息)
        'dev': {
            'class': 'logging.Formatter',
            'format': DEFAULT_FORMAT,
        },

    },
    # 处理器(被loggers使用)
    'handlers': {
        'console': {  # 按理来说, console只收集ERROR级别的较好
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'dev'
        },

    },
    # 真正的logger(by name), 可以有丰富的配置
    'loggers': {
        _CONSOLE_LOGGER_NAME: {
            'handlers': ['console', ],
            'level': 'INFO'
        }
    },
})

CONSOLE = logging.getLogger(_CONSOLE_LOGGER_NAME)
