# python-codes
The repository is the record of some python codes.

#爬取网址页面分析

1.网址分析

https://mhwg.org
wiki内容爬取，网页整体静态页，地址包含data 及 ida 两类，地址都是相对地址/开头，部分地址有#做锚点，其他地址主要是bbs，资源服务器，广告地址；部分页面结果是htm，发现页面都是404，需考虑过滤或者补充htm至html

2.网页内容分析

页面头部通用信息，中部包含文字内容及广告，底部无相关内容
页面整体utf8格式，日文格式，需要考虑转译中文，需要考虑有对照表
图片，js，css等资源都在其他服务器地址上，相关资源下载后，需要考虑网页内容替换成新地址

3.爬取流程考虑

入口获取页面-4层页面爬取url-保存4层内页面地址-单页面下载循环执行-过滤重复资源-下载完成（html部分 - 资源部分）

4.爬取后整理

html部分
需要有公共的头部及底部
需要整理内部链接地址
需要去除广告部分
需要翻译页面内容日文部分文案

资源部分
整理打包，原文件目录放置上传，不做调整
