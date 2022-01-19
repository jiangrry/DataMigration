# !/user/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/1/10 9:31
# @Author : jiangrh
# @Site : 
# @File : comparedfile.py
# @SoftWare : PyCharm


import json
import xlrd

# 读取文件
# with open('E:\\Work\\HZYY\\csv\\MySQL\\') as f1,open() as f2:


t = ''
with open('test.txt') as f1:
    t = f1.read()
    # print(t)
    # print(type(t))

t_double = t.replace("'",'"')
# t_double_add = t_double.join("},")
# t_double_add = t_double.join(t_double.replace("}","},"))
print(t_double)

# print(t_double_add)

t2d = json.loads(t_double)
print(t2d)

# t2d2 = eval(t_double)
# print(t2d2)
# print(type(t2d2))

# print(type(t2d))












# 根据读取到的文件进行数据比对
