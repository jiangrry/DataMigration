# !/user/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/1/13 14:04
# @Author : jiangrh
# @Site : 
# @File : ReadFile.py
# @SoftWare : PyCharm


import json
import pprint
from csv import DictReader
import os

def csv_to_dict(filename):
    try:
        with open(filename, 'r',encoding='utf-8') as read_obj:
            dict_reader = DictReader(read_obj)
            list_of_dict = list(dict_reader)
            result = json.dumps(list_of_dict, indent=2)
        return result
    except IOError as err:
        print("I/O error({0})".format(err))
#
# if __name__ == "__main__":
#     filename = os.path.join(os.path.abspath('./csv/MySQL'), 'evaluate_project.csv')
#     result = csv_to_dict(filename)
#     print(result)
