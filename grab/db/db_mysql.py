#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
    @Project: grab-client
    @Date: 1/10/2019 5:22 PM
    @Author: xuegangliu
    @Description: db_mysql
"""

import mysql.connector
import config.client_config as db_config

# 连接数据库
def get_mysql_conn():
    '''获取数据库连接'''
    conn = mysql.connector.connect(host=db_config.host,port=db_config.port,database=db_config.database,user=db_config.user,password=db_config.password,charset = 'utf8')
    return conn

# 执行sql
def execute_sql_by_params(sql,params):
    '''执行sql语句'''
    conn = get_mysql_conn()
    cursor = conn.cursor()
    cursor.execute(sql, params)
    print("table columns:%s" % str(cursor.column_names))
    list = cursor.fetchall()
    conn.close()
    return list

# 事物sql
def modify_sql_by_params(sql,params):
    '''执行sql语句'''
    conn = get_mysql_conn()
    conn.cursor().execute(sql, params)
    conn.commit()
    conn.close()

# 查询总数
def execute_sql_count_by_params(sql,params):
    '''获取sql总数'''
    conn = get_mysql_conn()
    cursor = conn.cursor()
    cursor.execute(sql, params)
    print("table columns:%s" % str(cursor.column_names))
    list = cursor.fetchall()
    conn.close()
    return len(list)