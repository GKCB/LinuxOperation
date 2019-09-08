#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   interaction.py
@Time    :   2019/09/08 11:32:51
@Author  :   CHENG Bo 
@Version :   1.0
@Contact :   hmkscbo@sina.com
@Github  :   https://github.com/GKCB
@Desc    :   None
'''

name   = input("name:")
age    = input("age:")
job    = input("job:")
salary = input("salary:")

#username = input("user name:")
#password = input("password:")
#print(username, password)

info = '''
-------- info of %s --------
Name:%s
Age:%s
Job:%s
Salary:%s
''' %(name, name, age, job, salary)

info2 = '''
-------- info of {_name} --------
Name:{_name}
Age:{_age}
Job:{_job}
Salary:{_salary}
''' .format(_name=name, 
            _age=age, 
            _job=job, 
            _salary=salary)

info3 = '''
-------- info of {0} --------
Name:{0}
Age:{1}
Job:{2}
Salary:{3}
''' .format(name, age, job, salary)

#print(info)
#print(info2)
print(info3)
