#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# date:        2019/5/26
# author:      he.zhiming
#

from __future__ import (absolute_import, unicode_literals)

from pyloggers import CONSOLE, make_file_logger, log

FILELOGGER = make_file_logger(__name__, filename="./LOGFILE.log")


def func(a, b, c):
    CONSOLE.info("====func start . {}====".format(locals()))
    try:
        raise ValueError("value error")
    except ValueError as e:
        CONSOLE.exception(e)


def test_a():
    CONSOLE.info("==== start ===")
    func(1, 1, 1)
    CONSOLE.info("==== end ==")


def test_file_logger():
    from pyloggers import _THREADLOCAL

    FILELOGGER.info("==== start ====")

    FILELOGGER.info("==== end ====")


@log
def add(a, b):
    return a + b


def test_log():
    add(1, 100)
