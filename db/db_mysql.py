#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
    @Project: grab-client
    @Date: 1/10/2019 5:22 PM
    @Author: xuegangliu
    @Description: db_mysql
"""

import mysql.connector

def get_mysql_conn(host,port,database,user,password):
    conn = mysql.connector.connect(host=host,port=port, database=database, user=user,password=password)
    return conn

def get_sql_list_by_id(host,port,database,user,password,sql,id):
    conn = get_mysql_conn(host,port,database,user,password)
    cursor = conn.cursor()
    cursor.execute(sql, id)
    list = cursor.fetchall()
    conn.close()
    return list