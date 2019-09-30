#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# date:        DATE
# author:      he.zhiming
#

from __future__ import (absolute_import, unicode_literals)
import codecs

import setuptools
from pyloggers import __version__


def _get_readme():
    with codecs.open("./README.rst", encoding="utf-8", mode="rb") as f:
        return f.read()


setuptools.setup(
    name="pyloggers",
    version=__version__,
    author="he.zhiming",
    author_email="he.zhiming@foxmail.com",
    description="loggers for Python2&3",
    long_description=codecs.open('README.rst', mode='r', encoding='utf-8').read(),
    url="https://github.com/hezhiming/pyloggers",
    packages=setuptools.find_packages(exclude=['./tests']),
    classifiers=[
        'Programming Language :: Python :: 2.7',
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        'Intended Audience :: Developers',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],
)
