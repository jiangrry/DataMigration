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


# import datetime

# dic0 = {"id": "4d834ba0525f451d88767696774d3b4a", "name": "升级项目005-OPT问题代码", "project_start_date": None,
#         "project_end_date": datetime.date(2022, 1, 13), "data_start_date": datetime.date(2021, 11, 2),
#         "data_end_date": datetime.date(2021, 11, 2), "status": 3, "create_user_id": -200,
#         "create_date": datetime.datetime(2022, 1, 13, 15, 52, 19),
#         "update_date": datetime.datetime(2022, 1, 13, 16, 8, 53), "type": 1, "take_user_id": -200,
#         "take_date": datetime.datetime(2022, 1, 13, 16, 7, 1), "project_name_version": 0}
# dic1 = {"id": 49, "name": "升级项目005-OPT问题代码", "type": 1, "data_start_date": datetime.date(2021, 11, 2),
#         "data_end_date": datetime.date(2021, 11, 2), "project_start_date": datetime.date(2022, 1, 13),
#         "project_end_date": datetime.date(2022, 1, 13), "take_user_id": -200, "take_user_name": "admin", "status": 8,
#         "template_id": 2, "create_time": datetime.datetime(2022, 1, 13, 15, 52, 19), "create_uid": -200,
#         "modified_time": datetime.datetime(2022, 1, 13, 17, 37, 27), "modified_uid": -100, "zone_ids": None,
#         "review_notice": 0, "finished_notice": 1}


def cmp_diff(dict1, dict2):
    differ_value = set(dict1.items()) ^ set(dict2.items())  # 字典不同的键值对
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

# differ_value = cmp_diff(dict1, dict2)
# print('字典不同的键值对:{0}'.format(differ_value))
# print('- - - 这是分隔符 - - - ')
# share_key = cmp_share(dict1, dict2)
# print('字典共有的键:{0}'.format(share_key))
# print('- - - 这是分隔符 - - - ')
# Not_shared = Not_shared(dict1, dict2)
# print('字典不共有的键:{0}'.format(Not_shared))
# print('- - - 这是分隔符 - - - ')
# onyl1 = onyl1(dict1, dict2)
# print('查看只在dict1中而dict2中没有的键:{0}'.format(onyl1))
# print('- - - 这是分隔符 - - - ')
# both = both(dict1, dict2)
# print('查看字典dict1和字典dict2相同的键值对:{0}'.format(both))


