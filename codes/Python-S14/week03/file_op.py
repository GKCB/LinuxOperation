#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   file_op.py
@Time    :   2019/09/16 12:03:54
@Author  :   CHENG Bo 
@Version :   1.0
@Contact :   hmkscbo@sina.com
@Github  :   https://github.com/GKCB
@Desc    :   None
'''

'''
#data = open("yesterday",encoding="utf-8").read()
f = open("yesterday2",'a',encoding="utf-8") #文件句柄
#a = append 追加

f.write("\nwhen i was young i listen to the radio\n")
data = f.read()
print('--read',data)

f.close()
'''

#f = open("yesterday2",'r+',encoding="utf-8") #文件句柄 读写
'''
f = open("yesterday2",'wb') #文件句柄  二进制文件
f.write("hello binary\n".encode())
'''

f.close()




'''

print(f.encoding)

#print(f.flush())
print(dir(f.buffer) )
#high bige

count = 0
for line in f:
    if count == 9:
        print('----我是分割线----------')
        count += 1
        continue
    print(line)
    count +=1

#low loop

for index,line in enumerate(f.readlines()):
    if index == 9:
        print('----我是分割线----------')
        continue
    print(line.strip())
#for i in range(5):
#    print(f.readline())
'''
