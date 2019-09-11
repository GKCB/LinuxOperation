
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

names = ["Zhang","Li","Wang","Qian"]
print(names[0:2])
print(names[-1])  #最后一个
print(names[-2:]) #最后两个
print(names[:3])  #前三个，0可以忽略
names.append("ll") #末尾添加
print(names)
