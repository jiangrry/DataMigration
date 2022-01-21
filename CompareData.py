# !/user/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/1/10 9:31
# @Author : jiangrh
# @Site : 
# @File : comparedfile.py
# @SoftWare : PyCharm

import os, sys
import re


# reload(sys)
# sys.setdefaultencoding("utf8")

# dct0 = {"name": "zhang", "age": "23"}
# dct1 = {"name": "san", "age": "23", "sex": "1"}
# print("字典dct0的值：" + str(dct0))
# print("字典dct1的值：" + str(dct1))
#
# differ = set(dct0.items()) ^ set(dct1.items())
# print("字典不同的值：")
# print(differ)
#
# print("查看字典dct0和字典dct1共有的key")
# print(set(dct0.keys()) & set(dct1.keys()))
#
# print("查看字典dct0和字典dct1不共有的key")
# print(set(dct0.keys()) ^ set(dct1.keys()))
#
# print("查看在字典dct1里面而不在字典dct0里面的key:")
# print(set(dct1.keys()) - set(dct0.keys()))
#
# print("查看字典dct0和字典dct1相同的键值对:")
# print(set(dct0.items()) & set(dct1.items()))
#
# dct0 = {"name": "zhang", "age": "23"}
# dct1 = {"name": "san", "age": "23", "sex": "1"}


def cmp_diff(dict1, dict2):
    differ_value = set(dict1.items()) ^ set(dict2.items())  # 字典不同的值
    return differ_value


def cmp_share(dict1, dict2):
    share_key = set(dict1.keys()) & set(dict2.keys())  # 字典共有的Key
    return share_key


def Not_shared(dict1, dict2):
    Not_shared = set(dict1.keys()) ^ set(dict2.keys())  # 字典不共有的Key
    return Not_shared


def onyl1(dict1, dict2):
    onyl1 = set(dict1.keys()) - set(dict2.keys())  # 查看在字典dct1里面而不在字典dct0里面的key
    return onyl1


def both(dict1, dict2):
    both = set(dict1.items()) & set(dict2.items())
    return both

# differ_value = cmp_diff(dct1, dct0)
# print('字典不同的值:{0}'.format(differ_value))
# share_key = cmp_share(dct1, dct0)
# print('字典共有的Key:{0}'.format(share_key))
# Not_shared = Not_shared(dct1, dct0)
# print('字典不共有的Key:{0}'.format(Not_shared))
# onyl1 = onyl1(dct1, dct0)
# print('查看在字典dct1里面而不在字典dct0里面的key:{0}'.format(onyl1))
# both = both(dct1, dct0)
# print('查看字典dct0和字典dct1相同的键值对:{0}'.format(both))
