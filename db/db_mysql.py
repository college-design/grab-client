#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
    @Project: python
    @Date: 8/31/2018 5:22 PM
    @Author: xuegangliu
    @Description: mysql_test
"""

import mysql.connector
import mysql.connector

def mysql_connect_init(host,user,password,database):
    conn = mysql.connector.connect(host=host,user=user, password=password, database=database)
    cursor = conn.cursor()
    cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
    cursor.execute('insert into user (id, name) values (%s, %s)', ['1', 'Michael'])
    cursor.rowcount
    conn.commit()
    conn.close()

def mysql_connect_get(host,user,password,database,id):
    conn = mysql.connector.connect(host=host,user=user, password=password, database=database)
    cursor = conn.cursor()
    cursor.execute(' select * from user where id=%s', id)
    list = cursor.fetchall()
    conn.close()
    return list

if __name__ == '__main__':
    host='127.0.0.1'
    user='root'
    password=''
    database='test'
    id=[1]
    list = mysql_connect_get(host=host,user=user,password=password,database=database,id=[1])
    print(list)