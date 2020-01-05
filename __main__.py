# !/usr/bin/env python
#vim: set fileencoding:utf-8

#***************************************************
# * Author         :  ZangDezhi
# * Email          :  winzdz@hotmail.com
# * Create Time    : 2019-12-17 21:17
# Last Modified  : 2020-01-05 23:25:43
# * FileName       : run.py
#**************************************************

import json     
import re      
import requests
import io
from requests import RequestException

# 传入 url 将抓去页面结果返回
def get_page(url):
    try:
        response = requests.get(url)
        #print(response) 
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None

#解析网页字符串
def parse_page(html):
    print("parse_page______")
    #生成一个正则表达式
    pattern = re.compile('<ul.*?class="one".*?([a-z0-9_-]{10}).*?class="two".*?[.\n].*?red">(.*?)</span>.*?red">(.*?)</span>.*?red">(.*?)</span>.*?red">(.*?)</span>.*?red">(.*?)</span>.*?red">(.*?)</span>.*?blue">(.*?)</span>.*?/li>', re.S)
   # pattern = re.compile('<li.*?one.*?[.\n](.*?).*?>', re.S)
   # pattern = re.compile('<ul.*?class="one".*?[.\n](.*?).*?class="two".*?[.\n].*?red">(.*?)</span>', re.S)
    #pattern = re.compile('<ul.*?class="one".*?[.\n](.*?).*?class="two".*?[.\n].*?red">(.*?)</span>.*?red">(.*?)</span>', re.S)

    #在字符串中查找匹配店所有子串,返回一个列表
    items = re.findall(pattern, html)
    print(len(items))
    i=0 
    L=[]
    for item in items:
        i+=1
       # print(item[2].decode("utf-8").encode("gbk"))
       # print(i)
        L.append(item[0].decode("utf-8")+","+
             item[1].decode("utf-8")+","+
             item[2].decode("utf-8")+","+
             item[3].decode("utf-8")+","+
             item[4].decode("utf-8")+","+
             item[5].decode("utf-8")+","+
             item[6].decode("utf-8")+","+
             item[7].decode("utf-8"))
    return L
def write_to_file(content):
    with io.open('AAAA.txt', 'a', encoding='utf-8')as f:
        f.write(unicode(content + "\n"))


def main():
    print("start---------------\n")

    url = "http://3g.henanfucai.com/Kais.do?id=9"
    html = get_page(url)
    for item in parse_page(html):
        print(item)
        write_to_file(item)
    print("end---------------\n")

if __name__ == '__main__':
        main()
