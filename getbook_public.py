#python 2.7
# coding: utf8
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
from bs4 import BeautifulSoup
import time
import urllib2

import urllib


import sys,os
sys.path.append(r'./')
from re_book import re_book
from save_info_txt import save_info_txt

book_list=[]
# book_list.append({'bookname':'一厘米的阳光','book_url':'https://www.2kxs.com/xiaoshuo/71/71295/'})
# book_list.append({'bookname':'等你的星光','book_url':'https://www.2kxs.com/xiaoshuo/80/80804/'})
# book_list.append({'bookname':'每天都在征服情敌','book_url':'https://www.2kxs.com/xiaoshuo/90/90405/'})
# book_list.append({'bookname':'天道图书馆','book_url':'https://www.208xs.com/dingdian/19_19376/'})
# book_list.append({'bookname':'里表世界','book_url':'https://www.biquge.cm/10/10263/'})
# book_list.append({'bookname':'修真聊天群','book_url':'http://www.biquge.cm/0/814/'})
# book_list.append({'bookname':'全球高武','book_url':'http://www.biquge.cm/11/11856/'})
# book_list.append({'bookname':'超神建模师','book_url':'http://www.biquge.cm/1/1615/'})
# book_list.append({'bookname':'我有一座恐怖屋','book_url':'https://www.booktxt.net/9_9554/'})
# book_list.append({'bookname':'恐怖邮差','book_url':'https://www.booktxt.net/7_7211/'})
# book_list.append({'bookname':'黎明之剑','book_url':'https://www.bequge.com/11_11147/'})
# book_list.append({'bookname':'太初','book_url':'https://www.booktxt.net/4_4097/'})
# book_list.append({'bookname':'诡秘之主','book_url':'https://www.biquge.info/3_3746/'})
# book_list.append({'bookname':'全职高手','book_url':'https://www.qb5200.tw/xiaoshuo/12/12521/'})
# book_list.append({'bookname':'全职法师','book_url':'http://www.booktxt.net/0_595/'})
book_list.append({'bookname':'大医凌然','book_url':'https://www.bequge.com/10_10855/'})


class GetBook:
    pageNum=1
    pageSize=3000
    book_file=''
    book_domian = ''
    endfilenamepath=''
    re_book=''
    save_info_txt=''

    def setBookFile(self,bookname,book_url):
        self.book_file = './' + bookname + '/'
        self.pageNum = 1
        self.endfilenamepath = self.book_file.decode('utf-8') + 'end.txt'
        self.re_book = re_book()
        self.save_info_txt = save_info_txt()
        self.book_domian = self.re_book.getBookDomain(book_url)

        if not os.path.exists(self.book_file.decode('utf-8')):
            os.makedirs(self.book_file.decode('utf-8'))
        return

    def getBookList(self,book_url):
        # print book_url
        connect = self.getUrlRead(book_url)
        list = []
        soup = BeautifulSoup(connect, "html.parser")
        # print self.book_domian
        if(self.book_domian == 'www.2kxs.com'):
            dd_list = soup.find("dl", class_="book").find_next_siblings("dd")
            for dd_info in dd_list:
                a_href = dd_info.find('a').get('href')
                if (a_href[0:1].isdigit()):
                    str = {'url': a_href}
                    list.append(str)
        elif(self.book_domian == 'www.x23us.com'):
            for bookinfo in soup.find_all("td"):
                if(bookinfo.find("a")) :
                    str = {'url':bookinfo.find("a")["href"]}
                    list.append(str)
        elif (self.book_domian == 'www.208xs.com'):
            # div_list = soup.find("div", _class="article_texttitleb");
            for bookinfo in soup.find("div", class_="article_texttitleb").find_all("a"):
                str = {'url':bookinfo["href"]}
                list.append(str)

        elif (self.book_domian == 'www.biquge.cm' or self.book_domian == 'www.kbiquge.cm'):
            # div_list = soup.find("div", _class="article_texttitleb");
            for bookinfo in soup.find("div", id="list").find_all("a"):
                str = {'url':bookinfo["href"]}
                list.append(str)
        elif ( self.book_domian == 'www.bequge.com' or self.book_domian=='www.biquge.info'):
            # div_list = soup.find("div", _class="article_texttitleb");
            for bookinfo in soup.find("div", id="list").find_all("a"):
                str = {'url':bookinfo["href"]}
                list.append(str)
        elif ( self.book_domian == 'www.booktxt.net'):
            # div_list = soup.find("div", _class="article_texttitleb");
            for bookinfo in soup.find("div", id="list").find_all("a"):
                str = {'url':bookinfo["href"]}
                list.append(str)
        elif ( self.book_domian == 'www.qb5200.tw'):
            # div_list = soup.find("div", _class="article_texttitleb");
            for bookinfo in soup.find("div", class_="listmain").find_all("a"):
                str = {'url':bookinfo["href"]}
                list.append(str)
        return list

    def getBookInfo(self,bookname,book_url):
        self.setBookFile(bookname,book_url)
        list = self.getBookList(book_url)
        endList = self.save_info_txt.getFileForLines(self.endfilenamepath)

        try:
            for book_chapter in list:
                self.pageNum = self.pageNum + 1
                if (self.book_domian == 'www.qb5200.tw' or self.book_domian == 'www.208xs.com' or self.book_domian == 'www.biquge.cm' or self.book_domian == 'www.kbiquge.cm' or self.book_domian == 'www.bequge.com'):
                    book_chapter_url = 'https://'+self.book_domian + book_chapter['url']
                else:
                    book_chapter_url = book_url + book_chapter['url']

                if ((book_chapter_url + '\n') in endList):
                    print "end:" + book_chapter_url
                    continue
                # time.sleep(0.5)
                # time.sleep(2)
                print book_chapter_url
                book_chapter_content = self.getAbook(book_chapter_url)
                booknamenum = bookname + str(int(self.pageNum / self.pageSize)) + '.txt'
                filenamepath = self.book_file.decode('utf-8') + booknamenum.decode('utf-8')
                self.save_info_txt.saveFileConnect(filenamepath, book_chapter_content)
                self.save_info_txt.saveFileConnect(self.endfilenamepath, book_chapter_url)
        # except urllib.error.URLError as e:
        except  urllib2.URLError as e:

            print 'url error try again'
            print e.reason
            time.sleep(20)
            self.getBookInfo(bookname,book_url)
        else:
            print 'other error try again'
        return True


    def getAbook(self,book_chapter_url):

        connect =  self.getUrlRead(book_chapter_url)
        bookinfo = {}
        soup = BeautifulSoup(connect, "html.parser")

        # print soup
        # 获取章节及内容
        if (self.book_domian == 'www.2kxs.com'):
            book_chapter_name = soup.find('h2').string
            # print book_chapter_name
            book_chapter_content = soup.find('p', class_='Text')
            # print book_chapter_content
            [s.extract() for s in book_chapter_content('a')]
            [s.extract() for s in book_chapter_content('font')]
            [s.extract() for s in book_chapter_content('script')]
            [s.extract() for s in book_chapter_content('strong')]
            # print book_chapter_name
            # print book_chapter_content.text
        elif (self.book_domian == 'www.x23us.com'  ):
            book_chapter_name = soup.find("div", id="amain").h1.string
            book_chapter_content = soup.find(id="contents")
        elif (self.book_domian == 'www.208xs.com'):
            book_chapter_name = soup.find("div",class_="book_content_text").h1.string
            book_chapter_content = soup.find(id="book_text")
        elif (self.book_domian == 'www.biquge.cm' or self.book_domian == 'www.kbiquge.cm' or self.book_domian == 'www.bequge.com'):
            book_chapter_name = soup.find("div", class_="bookname").h1.string
            book_chapter_content = soup.find(id="content")
        elif (self.book_domian == 'www.booktxt.net' or self.book_domian=='www.biquge.info' ):
            book_chapter_name = soup.find("div","bookname").h1.string
            book_chapter_content = soup.find(id="content")
        elif (self.book_domian == 'www.qb5200.tw' ):
            book_chapter_name = soup.find("div",class_="content").h1.string
            book_chapter_content = soup.find(id="content")
        content_capternumber = '【第'+ str(self.pageNum) +'章】 '

        book_chapter_name=  self.re_book.SubPunctuation(book_chapter_name)
        print content_capternumber
        print book_chapter_name

        book_chapter_content=self.re_book.filter_tags(book_chapter_content.encode('utf-8'))
        # print book_chapter_content
        book_chapter_content =content_capternumber + book_chapter_name.encode('utf-8')+'\n'+book_chapter_content+'\n'
        return book_chapter_content


    def testgetBookInfo(self, bookname, book_url):
        self.setBookFile(bookname, book_url)
        print book_url
        list = self.getBookList(book_url)
        endList = self.save_info_txt.getFileForLines(self.endfilenamepath)
        print list
        for book_chapter in list:
            print book_chapter
            self.pageNum = self.pageNum + 1
            if (self.book_domian == 'www.qb5200.tw'):
                book_chapter_url = 'https://' + self.book_domian + book_chapter['url']
                print book_chapter_url
            else:
                book_chapter_url = book_url + book_chapter['url']

            if ((book_chapter_url + '\n') in endList):
                print "end:" + book_chapter_url
                continue
            # time.sleep(0.5)
            print book_chapter_url
            book_chapter_content = self.getAbook(book_chapter_url)

            booknamenum = bookname + str(int(self.pageNum / self.pageSize)) + '.txt'
            filenamepath = self.book_file.decode('utf-8') + booknamenum.decode('utf-8')
            self.save_info_txt.saveFileConnect(filenamepath, book_chapter_content)
            self.save_info_txt.saveFileConnect(self.endfilenamepath, book_chapter_url)

        return True

    def getUrlRead(self,url):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
        req = urllib2.Request(url, headers=headers)
        connect = urllib2.urlopen(req).read()
        return connect
booktask = GetBook()

for bookinfo in book_list:
    booktask.getBookInfo(bookinfo['bookname'],bookinfo['book_url'])
    # booktask.testgetBookInfo(bookinfo['bookname'],bookinfo['book_url'])

#
