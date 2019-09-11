
#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   sys_mod.py
@Time    :   2019/09/11 16:01:31
@Author  :   CHENG Bo 
@Version :   1.0
@Contact :   hmkscbo@sina.com
@Github  :   https://github.com/GKCB
@Desc    :   None
'''

msg = "我爱北京天安门"
print(msg)
print(msg.encode(encoding="utf-8"))
print(msg.encode(encoding="utf-8").decode(encoding="utf-8"))
