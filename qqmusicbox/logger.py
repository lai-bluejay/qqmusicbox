#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
qqmusicbox/logger.py was created on 2019/03/31.
file in :relativeFile
Author: Charles_Lai
Email: lai.bluejay@gmail.com
"""
from __future__ import print_function, unicode_literals, division, absolute_import
import logging

from future.builtins import open

from qqmusicbox import const

FILE_NAME = const.Constant.log_path


with open(FILE_NAME, "a+") as f:
    f.write("#" * 80)
    f.write("\n")


def getLogger(name):
    log = logging.getLogger(name)
    log.setLevel(logging.DEBUG)

    # File output handler
    fh = logging.FileHandler(FILE_NAME)
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(
        logging.Formatter(
            "%(asctime)s - %(levelname)s - %(name)s:%(lineno)s: %(message)s"
        )
    )
    log.addHandler(fh)

    return log
