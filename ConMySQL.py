# !/user/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/1/9 11:16
# @Author : jiangrh
# @Site : 
# @File : conn_mysqlok.py
# @SoftWare : PyCharm

# coding=utf-8

# coding=utf-8

import pymysql as MySQLdb  # 这里是python3  如果你是python2.x的话，import MySQLdb
import pandas as pd
import os

host = '10.1.1.173'
# host = '10.1.1.174' # 当前服务器使用的174
user = 'yyuser'
password = 'iPh@23ysq!'
database = 'ipharmacare_review'


class SelectMySQL(object):

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
            cur.execute(sql)
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


if __name__ == '__main__':
    sql = "SELECT * FROM `ipharmacare_review`.evaluate_sample_data WHERE project_id in (SELECT id FROM `ipharmacare_review`.evaluate_project WHERE name IN ('升级项目005-OPT问题代码','升级项目006-IPT问题代码','升级项目007-OPT少量','升级项目008-IPT少量'));"
    select = SelectMySQL()
    result1 = select.get_result(sql, 'E:/Work/HZYY/DataMigration/txt/MySQL/evaluate_sample_data_assign.txt')
    print(result1)

t = result1
df = pd.DataFrame(t)
print(df)


df.to_csv('E:/Work/HZYY/DataMigration/csv/MySQL/evaluate_sample_data_assign.csv', index=True, header=True)
