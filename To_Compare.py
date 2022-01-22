# !/user/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/1/22 18:29
# @Author : jiangrh
# @Site : 
# @File : Data_Conversion.py
# @SoftWare : PyCharm

# 这个文件是为了将数据库获取的数据进行转换，从列表变更成字典

import datetime
from ConncetDB import Conncent_DB
import pandas as pd
from Csv_to_dict import csv_to_dict
from Compare_dict import cmp_diff, cmp_share, Not_shared, onyl1, both

if __name__ == '__main__':
    pgsql_host = '10.1.1.174'
    pgsql_user = 'yyuser'
    pgsql_password = 'iPh@23ysq!'
    pgsql_database = 'review_3to4_upgrade_test'
    # database = 'ipharmacare_review'
    pgsql_sql = "SELECT * FROM review_3to4_upgrade_test.evaluate.evaluate_project WHERE name IN ('升级项目005-OPT问题代码','升级项目006-IPT问题代码','升级项目007-OPT少量','升级项目008-IPT少量');"
    t2 = Conncent_DB.Con_PgSQL(pgsql_sql, pgsql_host, pgsql_user, pgsql_password, pgsql_database)

    df = pd.DataFrame(t2)
    # print(df)
    df.to_csv()
