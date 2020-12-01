# !/usr/bin/env python
# -!- coding: utf-8 -!-

#***************************************************
# * Author         :  ZangDezhi
# * Email          :  winzdz@hotmail.com
# * Create Time    : 2019-12-17 21:17
# Last Modified  : 2020-01-19 22:35:53
# * FileName       : run.py
#**************************************************

import json     
import re      
import requests
import io
import time
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
    #生成一个正则表达式
    pattern = re.compile(r'<ul.*?class="one".*?(\d\d\d\d-\d\d-[0-9]+).*?class="two".*?[.\n].*?red">(.*?)</span>.*?red">(.*?)</span>.*?red">(.*?)</span>.*?red">(.*?)</span>.*?red">(.*?)</span>.*?red">(.*?)</span>.*?blue">(.*?)</span>.*?/li>', re.S)
   # pattern = re.compile('<li.*?one.*?[.\n](.*?).*?>', re.S)
   # pattern = re.compile('<ul.*?class="one".*?[.\n](.*?).*?class="two".*?[.\n].*?red">(.*?)</span>', re.S)
   # pattern = re.compile('<ul.*?class="one".*?[.\n](.*?).*?class="two".*?[.\n].*?red">(.*?)</span>.*?red">(.*?)</span>', re.S)

    #在字符串中查找匹配店所有子串,返回一个列表
    items = re.findall(pattern, html)
    print(len(items))
    i=0 
    for item in items:
       # i+=1
       # print(item[2].decode("utf-8").encode("gbk"))
       # print(i)
        try:
        # Python3
             L.append(item[0]+","+
               item[1]+","+
               item[2]+","+
               item[3]+","+
               item[4]+","+
               item[5]+","+
               item[6]+","+
               item[7])
        except ImportError:
        # Python2
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
    with io.open('out.txt', 'a', encoding='utf-8')as f:
        try:
        # Python3
           f.write(str(content + "\n"))
        except ImportError:
        # Python2
           f.write(unicode(content + "\n"))


def main():

    print("start---------------\n")
    url = "http://3g.henanfucai.com/Kais.do?id=9"
    html = get_page(url)
    for num in range(1,20):  # 迭代 10 到 20 之间的数字
        time.sleep(0.1)
        url = "http://3g.henanfucai.com/KaiMore.do?id=9&pageno=%d"%(num)
        print (url)
        html += get_page(url)

    write_to_file("------------------")
    for item in parse_page(html):
        write_to_file(item)
    print("end---------------\n")

if __name__ == '__main__':
        main()
