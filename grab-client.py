#!/usr/bin/python
# -*- coding: UTF-8 -*-

import db.db_mysql as db_mysql
import config.client_config as db_config
import crawler.crawler_content as crawler_content

if __name__ == '__main__':
    print('Grab Client Start!!')
    sql = 'select * from web_site where id = %s'
    id=[1]
    list = db_mysql.get_sql_list_by_id(host=db_config.host,port=db_config.port,database=db_config.database,user=db_config.user,password=db_config.password,sql=sql,id=id)
    print(list[0][2])

    html=crawler_content.get_html(list[0][2])
    print(html)