#!/usr/bin/python
# -*- coding: UTF-8 -*-

import re

import db.db_mysql as db_mysql
import crawler.crawler_content as crawler_content

if __name__ == '__main__':
    print('############ Grab Client Start ###############')
    sql = 'select * from web_site where id = %s and url=%s'
    params=[1,'http://www.baidu.com']
    list = db_mysql.get_sql_list_by_params(sql=sql,params=params)
    # print(list)
    for t in range(len(list)):
        print(list[t][2])

    html=crawler_content.get_html(list[0][2])
    # print(html)

    # 获取链接
    rr = re.compile(r'href="(http://.*?)"')

    links = rr.findall(html)
    # print(links)
    for m in range(len(rr.findall(html))):
        print(links[m])
        insert_params=[links[m],m]
        db_mysql.execute_sql_by_params('insert into web_site (url,description) values (%s,%s)',insert_params)
    # print(len(db_mysql.get_sql_list_by_params('select count(1) from web_site ',[])))