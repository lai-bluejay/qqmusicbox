#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
qqmusicbox/__init__.py was created on 2019/03/31.
file in :relativeFile
Author: Charles_Lai
Email: lai.bluejay@gmail.com
"""

from qqmusicbox.utils import create_dir, create_file
from qqmusicbox.const import Constant

create_dir(Constant.conf_dir)
create_dir(Constant.download_dir)
create_file(Constant.storage_path)
create_file(Constant.log_path, default="")
create_file(Constant.cookie_path, default="#LWP-Cookies-2.0\n")
