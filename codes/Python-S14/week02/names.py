
#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   names.py
@Time    :   2019/09/11 16:35:39
@Author  :   CHENG Bo 
@Version :   1.0
@Contact :   hmkscbo@sina.com
@Github  :   https://github.com/GKCB
@Desc    :   None
'''
import copy

names = ["Zhang","Li","Wang","Qian"]
#name2 = names.copy() 
#只会copy一层 如果存在多层列表的话，下面的列表就没有被复制
#name2 = copy.copy(names) #和列表中的copy是一样的
name2 = copy.deepcopy(names)
print(names)
print(name2)
names[0] = "张"
print(names)
print(name2)
'''
print(names[0:2])
print(names[-1])  #最后一个
print(names[-2:]) #最后两个
print(names[:3])  #前三个，0可以忽略
names.append("ll") #末尾添加
print(names)
'''
