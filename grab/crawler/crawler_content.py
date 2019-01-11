#!/usr/bin/python
# -*- coding: UTF-8 -*-

from urllib import request
import chardet

def get_html(url):
    response = request.urlopen(url)
    html = response.read()
    print("网页的编码:",chardet.detect(html))
    html = html.decode("utf-8")
    return html