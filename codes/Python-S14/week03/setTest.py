#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   setTest.py
@Time    :   2019/09/14 22:31:20
@Author  :   CHENG Bo 
@Version :   1.0
@Contact :   hmkscbo@sina.com
@Github  :   https://github.com/GKCB
@Desc    :   None
'''

list_1 = [1,4,5,7,3,6,7,9]
list_1 = set(list_1) #已经是个集合了
#print(list_1,type(list_1))

list_2 = set([2,6,0,66,22,8,4])
print(list_1,list_2)

#交集
print("交集")
print(list_1.intersection(list_2))
print(list_1 & list_2)

#并集
print("并集") 
print(list_1.union(list_2))
print(list_1 | list_2)

#差集 in list1 not in list2
print("差集")
print(list_1.difference(list_2))
print(list_1-list_2)

#子集
print("子集")
list_3 = set([1,3,7])
print(list_3.issubset(list_1))

#父集
print("父集")
print(list_1.issuperset(list_3))

#对称差集 取出两个互相都没有的元素
print("对称差集")
print(list_1.symmetric_difference(list_2))
print(list_1^list_2)

#是否没有交集 没有返回True
print("")
print(list_1.isdisjoint(list_2))
list_4 = set([5,6,8])
print(list_3.isdisjoint(list_4))

list_1.add(999) #添加一项
list_1.update([888,777]) #添加多项

