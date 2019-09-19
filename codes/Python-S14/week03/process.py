#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   process.py
@Time    :   2019/09/16 16:57:48
@Author  :   CHENG Bo 
@Version :   1.0
@Contact :   hmkscbo@sina.com
@Github  :   https://github.com/GKCB
@Desc    :   None
'''

import sys,time

for i in range(20):
    sys.stdout.write("#")
    sys.stdout.flush()
    time.sleep(0.1)
