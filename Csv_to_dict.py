# !/user/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/1/13 14:04
# @Author : jiangrh
# @Site : 
# @File : ReadFile.py
# @SoftWare : PyCharm




import json
import os
import pprint


def csv_to_dict(filename):
    try:
        with open(filename, 'r',encoding='utf-8') as file:
            header, *lines = file.readlines()  # 读取文件数据（包含第一行列名）
            header = header.split(",")  # 第一行列名
            header = [i.strip() for i in header]  # 格式化
            lines = [i.strip() for i in lines]
            result = {}
            for counter, line in enumerate(lines):
                line_dict = {}
                for idx, item in enumerate(line.split(",")):
                    line_dict[header[idx]] = item
                result[str(counter)] = line_dict
            return result
    except IOError as err:
        print("I/O error({0})".format(err))

# if __name__ == "__main__":
#     filename = os.path.join(os.getcwd(), 'evaluate_project.csv')
#     result = csv_to_dict(filename)
#     # pprint.pprint(result)
#     print(json.dumps(result,indent=2))