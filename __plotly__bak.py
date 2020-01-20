
#!/usr/bin/env python
# -!- coding: utf-8 -!-

#***************************************************
# * Author         :  ZangDezhi
# * Email          :  winzdz@hotmail.com
# * Create Time    : 2020-01-09 15:55
# Last Modified  : 2020-01-20 22:48:05
# * FileName       : __plotly__.py
#**************************************************


#import plotly.graph_objects as go
#fig = go.Figure(data=go.Bar(y=[2, 3, 1]))
#fig.show()


import plotly as py
import plotly.graph_objs as go

pyplt = py.offline.plot

list_date = []
list_1= []
list_2= []
list_3= []
list_4= []
list_5= []
list_6= []
list_blue= []
num=-1
#[START]
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
#[END]
list_1 = list(map(int,list_1))
text1=[]
color1=[]
opacity1=[]
size1=[]
x1=[]
y1=[]
isize=10
for i in list_1:
    now = list_1[i]
    _text = "0 "
    _color = 100
    _opacity = 0.1
    _size = 10
    #[START]
    if y1.count(now) > 0:
      _index=y1.index(now)
      if _index >= 0:

          x1.pop(_index)
          y1.pop(_index)

          _text ="text" 
          text1.pop(_index)

          _color = color1[_index]
          color1.pop(_index)
         
          _opacity = opacity1[_index]
          opacity1.pop(_index)

          _size = size1[_index]
          size1.pop(_index)
    #[END]
    x1.append(0)
    y1.append(now)
    text1.append(_text)
    color1.append(_color)
    opacity1.append(_opacity)
    size1.append(_size)

trace_red0 = go.Scatter(
        x=x1,
        y=y1,
        mode='markers',
 
        #制订每个点,对应的悬浮文字提示信息(<br>标识换行);
        #text=['第1个气泡<br>size: 40<br>这里可以填写内容', '第2个气泡<br>size: 60', '第3个气泡<br>size: 80', '第4个气泡<br>size: 100'],
        text=text1,
        marker=dict(
        #指定每个点的颜色
        color=color1,
        #指定每个点的透明度
        opacity=opacity1,
        #指定每个点的大小
        size=size1,
        #标示右侧显示颜色条
        showscale= True
        )

    )



trace0 = go.Scatter(
 x=["red1", "red2", "red3", "red4","red5","red6","blue"],
 y=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,00],
 mode='markers',
 
 #制订每个点,对应的悬浮文字提示信息(<br>标识换行);
 text=['第1个气泡<br>size: 40<br>这里可以填写内容', '第2个气泡<br>size: 60', '第3个气泡<br>size: 80', '第4个气泡<br>size: 100'],
 marker=dict(

 #指定每个点的颜色
 color= [120, 125, 130, 135],

 #指定每个点的透明度
 opacity=[1, 0.8, 0.6, 0.4],

 #指定每个点的大小
 size=[40, 60, 80, 100],

 #标示右侧显示颜色条
 showscale= True,
 )
)
 
data = [trace_red0]
pyplt(data, filename='./1.html')



