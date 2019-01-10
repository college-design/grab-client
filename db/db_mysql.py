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

def get_mysql_conn():
    conn = mysql.connector.connect(host=db_config.host,port=db_config.port,database=db_config.database,user=db_config.user,password=db_config.password,charset = 'utf8')
    return conn

def get_sql_list_by_id(sql,id):
    conn = get_mysql_conn()
    cursor = conn.cursor()
    cursor.execute(sql, id)
    list = cursor.fetchall()
    conn.close()
    return list