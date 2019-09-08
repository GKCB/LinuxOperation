#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   passwd.py
@Time    :   2019/09/08 14:14:43
@Author  :   CHENG Bo 
@Version :   1.0
@Contact :   hmkscbo@sina.com
@Github  :   https://github.com/GKCB
@Desc    :   None
'''
import getpass

_username = "cheng"
_password = "abc123"
username = input("username:")
password = getpass.getpass("password:")

if _username == username and _password == password:
    print("Welcome user {name} login...".format(name=username))
else:
    print("Invalid username or password")

#print(username, password)
