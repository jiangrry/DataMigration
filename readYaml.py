# !/user/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/1/12 16:55
# @Author : jiangrh
# @Site : 
# @File : readYaml.py
# @SoftWare : PyCharm


import yaml
import os


#
# path = os.getcwd()
# print(path)
# path2 = os.chdir(path + '/db_conf')
# re2 = os.getcwd()
# print(re2)
#
# #
# def ReadYaml():
#     with open('db_conf/database_conf.yaml', 'r') as f:
#         file_content = f.read()
#
#
# content = yaml.load(file_content, yaml_FullLoader)
# print(content)
#
class ReadYaml:
    def __init__(self):
        # if file_path:
        #     self.file_path = file_path
        # else:
        root_dir = os.path.dirname(os.path.abspath('.'))

        # os.path.abspath('.')表示获取当前文件所在目录；os.path.dirname表示获取文件所在父目录；所以整个就是项目的所在路径
        # 可以修改 self.file_path 来调整或缺测试用所需要的测试数据
        self.file_path = root_dir + '\\db_conf\\database_conf.yaml'  # 获取文件所在的相对路径(相对整个项目) \\Ipharmacare

    def get_data(self):
        fp = open(self.file_path, encoding='utf-8')
        data = yaml.load(fp, Loader=yaml.FullLoader)
        yaml.warnings({'YAMLLoadWarning': False})
        return data


t = ReadYaml()
t1 = t.get_data('E:\Work\HZYY\Code\data_compare\db_conf\database_conf.yaml')
