#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   systest.py
@Time    :   2019/09/11 10:30:57
@Author  :   CHENG Bo 
@Version :   1.0
@Contact :   hmkscbo@sina.com
@Github  :   https://github.com/GKCB
@Desc    :   None
'''

'''
import sys
#print(sys.path)
print(sys.argv)
'''
import os
#cmd_res = os.system("dir") #执行命令，不保存
cmd_res = os.popen("dir") 
#cmd_res = os.popen("dir") 返回的是对象的内存地址
#需要再次的引用 read把结果读取出来
cmd_res = os.popen("dir").read()
print(cmd_res)

os.mkdir("new_dir") #创建目录
