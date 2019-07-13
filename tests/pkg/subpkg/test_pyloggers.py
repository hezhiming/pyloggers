#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# date:        2019/5/26
# author:      he.zhiming
#

from __future__ import (absolute_import, unicode_literals)

from pyloggers import make_file_logger

FILELOGGER = make_file_logger(__name__, filename=r"C:\hzm\FILELOG.log")

def func():
    try:
        raise ValueError("value error")

    except ValueError as e:
        FILELOGGER.exception(e)

def test_filelogger():
    FILELOGGER.info("==== start ====")
    for i in range(1000000):
        func()
    FILELOGGER.info("==== end ====")
