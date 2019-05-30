
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



def main():
    # 文件所在目录-存储文件夹-文件路径-获取文件-结束文件
    global SAVE_PATH
    # filePath = time.strftime('%Y-%m-%d', time.localtime()) + '-url-mhwg.org'
    filePath = 'url-mhwg.org'
    SAVE_PATH = os.path.join(SAVE_PATH, filePath)
    START_LIST_SAVE_TXT = os.path.join(SAVE_PATH, 'start.txt')
    END_LIST_SAVE_TXT = os.path.join(SAVE_PATH, 'end.txt')
    START_END_LIST_SAVE_TXT = os.path.join(SAVE_PATH, 'start_end.txt')



    if not os.path.exists(SAVE_PATH):
        print('> 目标目录不存在，创建：', SAVE_PATH)
        os.makedirs(SAVE_PATH)
    # save_info_txt
    # 采集到的地址，需要进行循环的获取，独立封装采集地址的方法
    # 需要构建采集的层级，避免无限采集
    # 需要登记已采集地址，避免重复采集

    start_list = save_info_txt.getFileForLines(START_LIST_SAVE_TXT)

    print(len(start_list))
    # 数组内去重
    start_list = list(set(start_list))
    # print(start_list)
    print(len(start_list))
    start_c_list = []
    for url in start_list:
        if (url.endswith('htm\n')):
            url = url.replace("htm\n", "html\n", 1)
            # print(url)
        start_c_list.append(url)

    start_c_list = list(set(start_c_list))
    print(len(start_c_list))
    # 已爬完页面去重
    end_list = save_info_txt.getFileForLines(END_LIST_SAVE_TXT)
    print(len(end_list))
    str_s = ''
    for s_url in start_c_list:
        str_s = str_s + s_url
    save_info_txt.saveFileConnect(START_END_LIST_SAVE_TXT, str_s)

if __name__ == '__main__':
    main()
    pass
