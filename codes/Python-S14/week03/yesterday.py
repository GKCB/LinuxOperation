#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   yesterday.py
@Time    :   2019/09/16 10:40:56
@Author  :   CHENG Bo 
@Version :   1.0
@Contact :   hmkscbo@sina.com
@Github  :   https://github.com/GKCB
@Desc    :   None
'''

#data = open("yesterday2",encoding="utf-8").read()

f = open("yesterday2","r",encoding="utf-8") #文件句柄
'''
data = f.read()
print(data)
'''

'''
for lines in f.readlines():
    print(lines.strip()) #去除多余的 '\n'
'''



f.close()
