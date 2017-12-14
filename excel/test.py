#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : test.py
# @Author: bruce
# @Date  : 2017/12/14
# @Desc  :

import os
print os.curdir
if os.path.isdir("source"):
    print "the dir is not empty"
else:
    os.mkdir("source")
if os.path.isdir("destination"):
    print "the dir is not empty"
else:
    os.mkdir("destination")


