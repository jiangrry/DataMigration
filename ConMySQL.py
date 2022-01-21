# !/user/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/1/9 11:16
# @Author : jiangrh
# @Site : 
# @File : conn_mysqlok.py
# @SoftWare : PyCharm

# coding=utf-8

# coding=utf-8
import json

import pymysql
import pymysql as MySQLdb  # 这里是python3  如果你是python2.x的话，import MySQLdb
import pandas as pd
import os
from Csv_to_dict import csv_to_dict

host = '10.1.1.173'
# host = '10.1.1.174' # 当前服务器使用的174
user = 'yyuser'
password = 'iPh@23ysq!'
database = 'ipharmacare_review'
port = 3306


class Data_MySQL(object):

    def select_data(self, sql):
        global cur, conn
        data_dict = {}
        try:
            conn = MySQLdb.connect(host=host,
                                   user=user,
                                   passwd=password,
                                   db=database,
                                   charset='utf8', )
            cur = conn.cursor()
            cur.execute(sql)  # 获取要查询的SQL
            col_result = cur.description  # 获取
            alldata = cur.fetchall()

            column = [index[0] for index in cur.description]
            data_dict = [dict(zip(column, row)) for row in alldata]


        except Exception as e:
            print('Error msg: ' + e)
        finally:
            cur.close()
            conn.close()

        return data_dict

    def get_result(self, sql, filename):
        print(sql)
        results = self.select_data(sql)
        print('The amount of datas: %d' % (len(results)))
        with open(filename, 'w') as f:
            for result in results:
                f.write(str(result) + '\n')
        print('Data write is over!')
        return results

    def read_txt(filename2):
        try:
            with open(filename2) as f1:
                content = f1.read()
                content_replace = content.replace("'", '"')
        except Exception as e2:
            print("Error msg:({0})".format(e2))
        return content_replace


    def txt2csv(content_replace, csv_path):
        # df = pd.DataFrame(content_replace)
        # return df.to_csv(csv_path, index=True, header=True)
        pass

    # def csv_to_dict(filename):
    #     pass


if __name__ == '__main__':
    sql = "SELECT * FROM `ipharmacare_review`.evaluate_sample_data WHERE project_id in (SELECT id FROM `ipharmacare_review`.evaluate_project WHERE name IN ('升级项目005-OPT问题代码','升级项目006-IPT问题代码','升级项目007-OPT少量','升级项目008-IPT少量'));"
    select = Data_MySQL()
    # 添加路径，文件名
    filename = os.path.join(os.path.abspath('.'), 'evaluate_sample_data_assign.txt')
    # filename = os.path.join(os.path.abspath('./txt/MySQL'), 'evaluate_sample_data_assign.txt')
    # print(filename)

    # result1 = select.get_result(sql, filename)
    # print(result1)

    # 读取导出的文件
    # filename2 = os.path.join(os.path.abspath('./txt/MySQL'), 'evaluate_sample_data_assign.txt')
    # # print(filename2)
    # rt = Data_MySQL.read_txt(filename2)
    # print(rt)

    # filename2 = os.path.join(os.path.abspath('.'), 'evaluate_sample_data_assign.txt')
    # result1 = Data_MySQL.txt2dict(filename2)
    # print(result1)

# # sql查询结果生成csv
# t = result1
# df = pd.DataFrame(t)
# print(df)
# csv_path = os.path.join(os.path.abspath('./csv/MySQL'), 'e.csv')
# df.to_csv(csv_path, index=True, header=True)

# class Data_MySQL():
#     def get_data(sql):
#         try:
#             connect = pymysql.Connect(host=host, user=user, password=password, db=database, port=port)
#             curses = connect.cursor()
#             curses.execute(sql)
#
#             col_result = curses.description  # 获取数据库表字段数据
#             rel = curses.fetchall()
#
#             column = [index[0] for index in curses.description]
#             data_dict = [dict(zip(column, row)) for row in rel]
#
#             curses.close()
#             connect.close()
#
#         except Exception as e:
#             print('- - - - - - ')
#             print("Error msg:({0})".format(e))
#             print('- - - - - - ')
#
#         return data_dict,column
#
#     def get_csv(data_dict, columns, csv_path):
#         data1 = list(map(list, data_dict))
#         df = pd.DataFrame(data=data1, columns=columns)
#         df.to_csv(csv_path,  index=True, header=True)
#
#
# if __name__ == '__main__':
#     sql = "SELECT * FROM `ipharmacare_review`.evaluate_sample_data WHERE project_id in (SELECT id FROM `ipharmacare_review`.evaluate_project WHERE name IN ('升级项目005-OPT问题代码','升级项目006-IPT问题代码','升级项目007-OPT少量','升级项目008-IPT少量'));"
#     result1,column = Data_MySQL.get_data(sql)
#     # print(result1)
#     # print(column)
#
#     csv_path = os.path.join(os.path.abspath('./csv'), '1.csv')
#     print(csv_path)
#     csvdata = Data_MySQL.get_csv(csv_path, result1, column)
