# !/user/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/1/22 13:38
# @Author : jiangrh
# @Site : 
# @File : ConncetDB.py
# @SoftWare : PyCharm

# 连接数据库 -- 方法
import pymysql as MySQLDB
import psycopg2 as PgSQLDB


class Conncent_DB():
    # def __init__(self,host,user,password,port,database):
    #     self.host = host
    #     self.user = user
    #     self.password = password
    #     self.port = port
    #     self.database = database

    def Con_MySQL(mysql, mysql_host, mysql_user, mysql_password, mysql_database):
        try:
            # 连接MySQL数据库
            connect_mysql = MySQLDB.connect(host=mysql_host,
                                            user=mysql_user,
                                            passwd=mysql_password,
                                            database=mysql_database,
                                            port=3306)
            curses_mysql = connect_mysql.cursor()
            curses_mysql.execute(mysql)
            all_mysql_data = curses_mysql.fetchall()

            column = [index[0] for index in curses_mysql.description]
            all_my_data = [dict(zip(column, row)) for row in all_mysql_data]

        # 如果连接异常，则抛出异常信息
        except Exception as error_mysql:
            return error_mysql

        finally:
            curses_mysql.close()
            connect_mysql.close()
        # 返回所有的查询MySQL的数据值
        return all_my_data

    def Con_PgSQL(pgsql, pgsql_host, pgsql_user, pgsql_password, pgsql_database):
        try:
            # 连接PgSQL数据库
            connect_pgsql = PgSQLDB.connect(host=pgsql_host,
                                            user=pgsql_user,
                                            password=pgsql_password,
                                            database=pgsql_database,
                                            port=5432)

            curses_pgsql = connect_pgsql.cursor()
            curses_pgsql.execute(pgsql)
            all_pgsql_data = curses_pgsql.fetchall()

            # 字段描述，表头
            column = [index[0] for index in curses_pgsql.description]
            all_pg_data = [dict(zip(column, row)) for row in all_pgsql_data]

        # 如果连接异常，则抛出异常信息
        except Exception as error_pgsql:
            return error_pgsql
        # 返回所有的查询PgSQL的数据值
        # finally:
        #     curses_pgsql.close()
        #     connect_pgsql.close()
        return all_pg_data


if __name__ == '__main__':
    mysql_host = '10.1.1.173'
    # host = '10.1.1.174' # 当前服务器使用的174
    mysql_user = 'yyuser'
    mysql_password = 'iPh@23ysq!'
    mysql_database = 'ipharmacare_review'

    mysql_sql = "SELECT * FROM `ipharmacare_review`.evaluate_project WHERE name IN ('升级项目005-OPT问题代码','升级项目006-IPT问题代码','升级项目007-OPT少量','升级项目008-IPT少量');"
    t = Conncent_DB.Con_MySQL(mysql_sql, mysql_host, mysql_user, mysql_password, mysql_database)
    # print(t)


    print(" = = = = = = = 这是一道分割线 = = = = = = = = ")
    print(" = = = = = = = 这是一道分割线 = = = = = = = = ")
    print(" = = = = = = = 这是一道分割线 = = = = = = = = ")
    print(" = = = = = = = 这是一道分割线 = = = = = = = = ")

    pgsql_host = '10.1.1.174'
    pgsql_user = 'yyuser'
    pgsql_password = 'iPh@23ysq!'
    pgsql_database = 'review_3to4_upgrade_test'
    # database = 'ipharmacare_review'
    pgsql_sql = "SELECT * FROM review_3to4_upgrade_test.evaluate.evaluate_project WHERE name IN ('升级项目005-OPT问题代码','升级项目006-IPT问题代码','升级项目007-OPT少量','升级项目008-IPT少量');"
    t2 = Conncent_DB.Con_PgSQL(pgsql_sql, pgsql_host, pgsql_user, pgsql_password, pgsql_database)
    print(t2)

    print(type(t2))