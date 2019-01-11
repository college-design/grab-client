#!/usr/bin/python
# -*- coding: UTF-8 -*-

import re

from grab.db import db_mysql as db_mysql
import grab.crawler.crawler_content as crawler_content

# 获取web_site数据
def get_web_site():
    return db_mysql.execute_sql_by_params('select * from web_site where status=1 ',[])

def get_grap_rule(id):
    return db_mysql.execute_sql_by_params('select * from grap_rule where status=1 and web_site_id=%s ',id)

def batch_job1():
    print('############ Grab Client Start ###############')
    list = get_web_site()
    print(len(list))
    for i in list:
        webId = [i[0]]
        webUrl = i[3]
        # print(webId)
        # print(webUrl)
        rule = get_grap_rule(webId)
        html= crawler_content.get_html(webUrl)
        for j in rule:
            grabRule=j[2]
            ruleId=j[0]
            rr = re.compile(grabRule)
            resultData = rr.findall(html)
            print(resultData)
            for k in resultData:
                params = []
                params.append(k)
                params.append(ruleId)
                db_mysql.modify_sql_by_params(r'insert into match_data (data,grab_rule_id) values (%s,%s)',params)
        db_mysql.modify_sql_by_params(r'update web_site set status=0 where id=%s',webId)
    print(db_mysql.execute_sql_count_by_params('select * from match_data',[]))