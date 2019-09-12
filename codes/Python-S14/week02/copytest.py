#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   copytest.py
@Time    :   2019/09/12 14:25:49
@Author  :   CHENG Bo 
@Version :   1.0
@Contact :   hmkscbo@sina.com
@Github  :   https://github.com/GKCB
@Desc    :   None
'''
import copy
person = ['name',['saving',100]]
'''
p1 = copy.copy(person)
p2 = person[:]    #也是一种浅copy
p3 = list(person) #工厂函数list
'''
p1 = person[:]
p2 = person[:]

p1[0] = "zhang"
p2[0] = "li"

print(p1)
print(p2)