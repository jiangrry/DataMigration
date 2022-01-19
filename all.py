# !/user/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/1/12 16:26
# @Author : jiangrh
# @Site : 
# @File : all.py
# @SoftWare : PyCharm
import os

import psycopg2 as PgMySQLdb
import pymysql as MySQLdb
from DataMigration.ConMySQL import SelectMySQL
from DataMigration.ConPgSQL import SelectPgSQL
# from DataMigration.CompareData import import
# 比较文件是否统一
# 读取数据库配置
import yaml

if __name__ == '__main__':
    # 查询sql
    sql = "SELECT * FROM `ipharmacare_review`.evaluate_project WHERE name IN ('升级项目001-OPT','升级项目002-IPT','升级项目003-OPT带申述','升级项目004-IPT带申述');"
    psql = "SELECT * FROM review_3to4_upgrade_test.evaluate.evaluate_project WHERE name IN ('升级项目001-OPT','升级项目002-IPT','升级项目003-OPT带申述','升级项目004-IPT带申述');"

    # 实例化查询方法
    select = SelectMySQL()
    select2 = SelectPgSQL()
    # 生成txt文件
    result1 = select.get_result(sql, 'E:/Work/HZYY/Code/DataMigration/data/test9.txt')
    result2 = select2.get_result(psql, 'E:/Work/HZYY/Code/DataMigration/data/test8.txt')

    print(result1)
    print(result2)
