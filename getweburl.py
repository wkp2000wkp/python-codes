#!/bin/usr/env python3
# -*- coding: utf-8 -*-

# 爬取网站url
#考虑爬取层数
#考虑地址去重

import ssl
ssl._create_default_https_context = ssl._create_unverified_context
from bs4 import BeautifulSoup
import time
from urllib import request
import re




def getUrlRead( url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
    req = request.Request(url, headers=headers)
    connect = request.urlopen(req).read()
    return connect

get_url_number = 3
get_url_entrance = 'http://mhwg.org'




def filterUrl(url):
    #当前站点网址都是/开头
    #http开头的，domain部分非mhwg.org都需要过滤
    REG_URL = '[/]'
    resourceUrlDict = re.match(REG_URL, url)
    if resourceUrlDict is None:
        return
    # print(resourceUrlDict)
    return get_url_entrance+url

def main():
    connect = getUrlRead(get_url_entrance)
    get_url_list = []
    soup = BeautifulSoup(connect, "html.parser")
    a_list = soup.find_all('a')
    for a_info in a_list:
        # print(a_info.find('a').get('href'))
        # print (a_info.get('href'))
        get_url = filterUrl(a_info.get('href'))
        if get_url  is not None:
            get_url_list.append(get_url)
    print(get_url_list)

if __name__ == '__main__':
    main()
    pass
