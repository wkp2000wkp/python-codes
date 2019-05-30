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
import save_info_txt
import os
from save_info_txt import save_info_txt

SAVE_PATH = os.path.join(os.path.abspath('.'), 'python-spider-downloads')

def getUrlRead( url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
    req = request.Request(url, headers=headers)
    connect = request.urlopen(req).read()
    return connect

get_url_number = 4
get_url_entrance = 'http://mhwg.org'




def filterUrl(url):
    #当前站点网址都是/开头
    #http开头的，domain部分非mhwg.org都需要过滤
    REG_URL = '[/]'
    #去除锚点信息
    REG_SEARCH_URL = '[#]'
    resourceUrlDict = re.match(REG_URL, url)
    if resourceUrlDict is None:
        return
    # print(resourceUrlDict)
    search_tup = re.search(REG_SEARCH_URL, url)
    if search_tup is not None:
        url = url[0:search_tup.span()[0]]
    return get_url_entrance + url

def gethreflist(url):
    connect = getUrlRead(url)
    get_url_list = []
    soup = BeautifulSoup(connect, "html.parser")
    a_list = soup.find_all('a')
    for a_info in a_list:
        # print(a_info.find('a').get('href'))
        # print (a_info.get('href'))
        get_url = filterUrl(a_info.get('href'))
        if get_url is not None:
            get_url_list.append(get_url)
    # print(get_url_list)
    return get_url_list



def main():
    # 文件所在目录-存储文件夹-文件路径-获取文件-结束文件
    global SAVE_PATH
    # filePath = time.strftime('%Y-%m-%d', time.localtime()) + '-url-mhwg.org'
    filePath = 'url-mhwg.org'
    SAVE_PATH = os.path.join(SAVE_PATH, filePath)
    START_LIST_SAVE_TXT = os.path.join(SAVE_PATH, 'start.txt')
    END_LIST_SAVE_TXT = os.path.join(SAVE_PATH, 'end.txt')

    if not os.path.exists(SAVE_PATH):
        print('> 目标目录不存在，创建：', SAVE_PATH)
        os.makedirs(SAVE_PATH)

    #初始化入口地址
    save_info_txt.saveFileConnect(START_LIST_SAVE_TXT,get_url_entrance)

    #确认爬取层数

    for i in range(0,get_url_number+1):
        print('当前爬取页面层数：',i)
    #获取全量待爬地址
        start_list = save_info_txt.getFileForLines(START_LIST_SAVE_TXT)
        #数组内去重
        start_list = list(set(start_list))
        # print(start_list)

        # 已爬完页面去重
        end_list = save_info_txt.getFileForLines(END_LIST_SAVE_TXT)
        # start_list,end_list
        start_c_list = []
        for i in start_list:
            if i not in end_list:
                start_c_list.append(i)
        #初始化进度显示
        url_num = 0
        start_count = len(start_c_list)
        for start_list_url in start_c_list:

            #采集查重-读取的url有换行符 - 独立换行符存在
            end_list = save_info_txt.getFileForLines(END_LIST_SAVE_TXT)
            # print(start_list_url)
            # print(end_list)
            # exit('the end')
            if ((start_list_url ) in end_list) :
                url_num += 1
                print('当前页面重复', url_num, '/', start_count, '：', start_list_url)
                continue

            url_num += 1
            print('当前页面',url_num,'/',start_count,'：' ,start_list_url)
            try:
                get_url_list = gethreflist(start_list_url)
            except Exception as e:
                print(e)
                print('当前页面错误', url_num, '/', start_count, '：', start_list_url)
                continue
            str_s = ''
            for s_url in get_url_list:
                #存储查重-抓取的url没有换行符
                if ((s_url + '\n') in end_list):
                    # print ('重复地址：',s_url)
                    continue
                str_s = str_s + s_url + '\n'
            if str_s != '' :
                str_s = str_s[0:-2]
                save_info_txt.saveFileConnect(START_LIST_SAVE_TXT, str_s)
            save_info_txt.saveFileConnect(END_LIST_SAVE_TXT, start_list_url.replace("\n", ""))



    # save_info_txt.getFileForLines(END_LIST_SAVE_TXT)

    # getFileForLines



    # gethreflist




    # save_info_txt
    # 采集到的地址，需要进行循环的获取，独立封装采集地址的方法
    # 需要构建采集的层级，避免无限采集
    # 需要登记已采集地址，避免重复采集


if __name__ == '__main__':
    main()
    pass
