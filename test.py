#!/bin/usr/env python3
# -*- coding: utf-8 -*-

# 爬取网站资源

__author__ = 'mask'

import urllib.request
import re
import os
import time
from functools import reduce


from io import BytesIO
import gzip
IMG_TYPE_ARR = ['jpg', 'png', 'ico', 'gif', 'jpeg', 'svg']

# 正则表达式预编译
# 这里涉及到了非贪婪匹配
# ((?:/[a-zA-Z0-9.]*?)*)
# ((?:/[a-zA-Z0-9.]*)*?)
REG_URL = r'^(https?://|//)?((?:[a-zA-Z0-9-_]+\.)+(?:[a-zA-Z0-9-_:]+))((?:/[-_.a-zA-Z0-9]*?)*)((?<=/)[-a-zA-Z0-9]+(?:\.([a-zA-Z0-9]+))+)?((?:\?[a-zA-Z0-9%&=]*)*)$'
REG_URL = r'^(https?://|//)?((?:[a-zA-Z0-9-_]+\.)+(?:[a-zA-Z0-9-_:]+))((?:/[-_.a-zA-Z0-9]*?)*)((?<=/)[-_.a-zA-Z0-9]+(?:\.([a-zA-Z0-9]+))+)?((?:\?[a-zA-Z0-9%&=]*)*)$'
# REG_URL = r'^(https?://|//)?((?:[a-zA-Z0-9-_]+\.)+(?:[a-zA-Z0-9-_:]+))((?:/[-_.a-zA-Z0-9]*)*?)((?<=/)[-a-zA-Z0-9]+(?:\.([a-zA-Z0-9]+))+)?((?:\?[a-zA-Z0-9%&=]*)*)$'
REG_RESOURCE_TYPE = r'(?:href|src|data\-original|data\-src)=["\'](.+?\.(?:js|css|jpg|jpeg|png|gif|svg|ico|ttf|woff2))[a-zA-Z0-9\?\=\.]*["\']'

regUrl = re.compile(REG_URL)
regResouce = re.compile(REG_RESOURCE_TYPE, re.S)


url = 'http://mhwg.org/'

# url = 'http://s.mhwg.org/assets/application-6bcfb9cf071a05e777567a3d26ed221b144f532e92e62c8d7dcf845ec732838e.css'
url = 'http://192.168.1.109:8080/abc/images/111/index.html?a=1&b=2'
# url = 'http://s.mhwg.org/mhw_icon.jpg'
# url = 'http://s.mhwg.org/images/parts/mhw_icon.jpg'

print("-----------",url)
res = regUrl.search(url)
for i in range(0,7) :
    print("group ",i," :", res.group(i))
# print("group 1 :", res.group(1))
# print("group 2 :", res.group(2))
# print("group 3 :", res.group(3))
# print("group 4 :", res.group(4))

url = 'http://s.mhwg.org/images/parts/mhw_icon.jpg'
print("-----------",url)
res = regUrl.search(url)
for i in range(0,7) :
    print("group ",i," :", res.group(i))

url = 'http://192.168.1.109:8080/abc/images/111/index.html?a=1&b=2'
url = 'http://192.168.1.109:8080/abc/ima_ges/111/mhw_icon.jpg'
print("-----------",url)
res = regUrl.search(url)
for i in range(0,7) :
    print("group ",i," :", res.group(i))



mhw_s='[/]'

url = '/data/44223.html'
print("-----------",url)
print (re.match(mhw_s,url))

url = 'http://192.168.1.109:8080/abc/ima_ges/111/mhw_icon.jpg'
print("-----------",url)
print (re.match(mhw_s,url))


mhw_s='[#]'

url = '/data/44223.html'
print("-----------",url)
print (re.search(mhw_s,url))


url = 'http://mhwg.org/data/4200.html#id1072'
print("-----------",url)
print(type (re.search(mhw_s,url).span()))

sear = re.search(mhw_s,url).span()
print( url[0:30])
print( url[0:re.search(mhw_s,url).span()[0]])

print ('\n'.isspace())
print("-----------",url)
url = 'http://mhwg.org/data/4200.html'
