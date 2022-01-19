# !/user/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/1/9 11:16
# @Author : jiangrh
# @Site :
# @File : conn_mysql2.py
# @SoftWare : PyCharm

# coding=utf-8

# coding=utf-8

import psycopg2 as PgMySQLdb
import json
import pandas as pd

host = '10.1.1.174'
user = 'yyuser'
password = 'iPh@23ysq!'
database = 'review_3to4_upgrade_test'
# database = 'ipharmacare_review'
port = '5432'


class SelectPgSQL(object):
    def select_data(self, sql):
        global cur, conn
        result = []
        try:
            conn = PgMySQLdb.connect(host=host,
                                     user=user,
                                     password=password,
                                     database=database,
                                     port=port)
            cur = conn.cursor()
            cur.execute(sql)
            alldata = cur.fetchall()
            # print(alldata)

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

    def get_csv_result(self, filename):
        pass


if __name__ == '__main__':
    sql = "SELECT * FROM review_3to4_upgrade_test.evaluate.evaluate_sample_data_statement WHERE project_id in (SELECT id FROM review_3to4_upgrade_test.evaluate.evaluate_project WHERE name in ('升级项目005-OPT问题代码','升级项目006-IPT问题代码','升级项目007-OPT少量','升级项目008-IPT少量'));"
    select = SelectPgSQL()
    # result1 = select.get_result(sql, 'E:/Work/HZYY/DataMigration/txt/PgSQL/evaluate_sample_data_statement.txt')
    result1 = select.get_result(sql, 'E:/Work/HZYY/DataMigration/txt/PgSQL/evaluate_sample_data_statement_test.csv')
    print(result1)

# t = result1
# df = pd.DataFrame(t)
# print(df)
#
# df.to_csv('E:/Work/HZYY/DataMigration/csv/PgSQL/evaluate_sample_data_statement.csv', index=True, header=True)
