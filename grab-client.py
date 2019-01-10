#!/usr/bin/python
# -*- coding: UTF-8 -*-

import re

import db.db_mysql as db_mysql
import crawler.crawler_content as crawler_content

if __name__ == '__main__':
    print('############ Grab Client Start ###############')
    sql = 'select * from web_site where id = %s and url=%s'
    id=[1,'http://www.baidu.com']
    list = db_mysql.get_sql_list_by_id(sql=sql,id=id)
    # print(list)
    for t in range(len(list)):
        print(list[t][2])

    html=crawler_content.get_html(list[0][2])
    # print(html)

    # 获取链接
    rr = re.compile(r'href="(.*?)"')
    print(rr.findall(html))
