#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import configparser

#获取文件的当前路径（绝对路径）
cur_path=os.path.dirname(os.path.realpath(__file__))


#获取config.ini的路径
config_path=os.path.join(cur_path,'grab.conf')


conf=configparser.ConfigParser()
conf.read(config_path)

db_host = conf.get("db", "db_host")
db_port = conf.getint("db", "db_port")
db_user = conf.get("db", "db_user")
db_pass = conf.get("db", "db_pass")
db_database = conf.get("db", "db_database")