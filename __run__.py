
#!/usr/bin/env python
# coding:utf-8

#***************************************************
# * Author         :  ZangDezhi
# * Email          :  winzdz@hotmail.com
# * Create Time    : 2020-01-07 19:07
# Last Modified  : 2020-01-20 14:53:38
# * FileName       : __run__.py
#**************************************************
import random

list_date = []
list_1= []
list_2= []
list_3= []
list_4= []
list_5= []
list_6= []
list_blue= []
num=-1

file = open("out.txt") 
while 1:
    line = file.readline()
    if not line:
        break
    line=line.split('\n')[0] 
    tmp=line.split(',')
    if len(tmp) == 8:
        num+=1
        list_date.append(tmp[0])
        list_1.append(tmp[1])
        list_2.append(tmp[2])
        list_3.append(tmp[3])
        list_4.append(tmp[4])
        list_5.append(tmp[5])
        list_6.append(tmp[6])
        list_blue.append(tmp[7])
    pass # do something
file.close()
for i in range(5):
    try:
        # Python2
        red1=list_1[ random.randint(0,num)]
        red2=list_2[ random.randint(0,num)]
        red3=list_3[ random.randint(0,num)]
        red4=list_4[ random.randint(0,num)]
        red5=list_5[ random.randint(0,num)]
        red6=list_6[ random.randint(0,num)]
        blue=list_blue[ random.randint(0,num)]
    except ImportError:
        # Python3
        red1=list_1[ random.randint(1,num)]
        red2=list_2[ random.randint(1,num)]
        red3=list_3[ random.randint(1,num)]
        red4=list_4[ random.randint(1,num)]
        red5=list_5[ random.randint(1,num)]
        red6=list_6[ random.randint(1,num)]
        blue=list_blue[ random.randint(1,num)]
    print (red1 +"," + red2 +"," + red3 + ","+ red4 + "," + red5 + "," + red6 + "," + blue)

