# !/user/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/1/13 14:04
# @Author : jiangrh
# @Site : 
# @File : ReadFile.py
# @SoftWare : PyCharm


import os


class ReadFile():
    def __init__(self, filename):
        self.filename = filename

    # 读取txt文件的方法
    def readtxtfile(filename):
        with open(filename, 'r') as f:
            data = f.read()
        return data


# filename = 'test.txt'
# ReadFile(filename)
# t = ReadFile.readtxtfile(filename)
# print(t)


