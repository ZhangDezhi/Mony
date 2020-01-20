
#!/usr/bin/env python
# -!- coding: utf-8 -!-

#***************************************************
# * Author         :  ZangDezhi
# * Email          :  winzdz@hotmail.com
# * Create Time    : 2020-01-09 15:55
# Last Modified  : 2020-01-20 23:37:53
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
i=0
for tmp in list_1:
    
    now = list_1[i]
    _color = 100
    _opacity = 0.5
    _size = 10
    _text = list_date[i] 
    i=i+1
    if y1.count(now) > 0:
    #[START]
      _index=y1.index(now)

      if _index >= 0:

          x1.pop(_index)
          x1.insert(_index,0)

          y1.pop(_index)
          y1.insert(_index,now)

          _text = text1[_index] + "</br>" + _text
          text1.pop(_index)
          text1.insert(_index,_text)

          _color += color1[_index]
          color1.pop(_index)
          color1.insert(_index,_color)
         
          _opacity = opacity1[_index]
          opacity1.pop(_index)
          opacity1.insert(_index,_opacity)

          _size = size1[_index] +5
          size1.pop(_index)
          size1.insert(_index,_size)
    #[END]
    else:
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


list_2 = list(map(int,list_2))
text2=[]
color2=[]
opacity2=[]
size2=[]
x2=[]
y2=[]
isize=10
i=0
for tmp in list_2:
    
    now = list_2[i]
    _color = 100
    _opacity = 0.5
    _size = 10
    _text = list_date[i] 
    i=i+1
    if y2.count(now) > 0:
    #[START]
      _index=y2.index(now)

      if _index >= 0:

          x2.pop(_index)
          x2.insert(_index,1)

          y2.pop(_index)
          y2.insert(_index,now)

          _text = text2[_index] + "</br>" + _text
          text2.pop(_index)
          text2.insert(_index,_text)

          _color += color2[_index]
          color2.pop(_index)
          color2.insert(_index,_color)
         
          _opacity = opacity2[_index]
          opacity2.pop(_index)
          opacity2.insert(_index,_opacity)

          _size = size2[_index] +5
          size2.pop(_index)
          size2.insert(_index,_size)
    #[END]
    else:
        x2.append(1)
        y2.append(now)
        text2.append(_text)
        color2.append(_color)
        opacity2.append(_opacity)
        size2.append(_size)


trace_red2 = go.Scatter(
        x=x2,
        y=y2,
        mode='markers',
 
        #制订每个点,对应的悬浮文字提示信息(<br>标识换行);
        #text=['第1个气泡<br>size: 40<br>这里可以填写内容', '第2个气泡<br>size: 60', '第3个气泡<br>size: 80', '第4个气泡<br>size: 100'],
        text=text2,
        marker=dict(
        #指定每个点的颜色
        color=color2,
        #指定每个点的透明度
        opacity=opacity2,
        #指定每个点的大小
        size=size2,
        #标示右侧显示颜色条
        showscale= True
        )

    )

list_3 = list(map(int,list_3))
text3=[]
color3=[]
opacity3=[]
size3=[]
x3=[]
y3=[]
isize=10
i=0
for tmp in list_3:
    
    now = list_3[i]
    _color = 100
    _opacity = 0.5
    _size = 10
    _text = list_date[i] 
    i=i+1
    if y3.count(now) > 0:
    #[START]
      _index=y3.index(now)

      if _index >= 0:

          x3.pop(_index)
          x3.insert(_index,2)

          y3.pop(_index)
          y3.insert(_index,now)

          _text = text3[_index] + "</br>" + _text
          text3.pop(_index)
          text3.insert(_index,_text)

          _color += color3[_index]
          color3.pop(_index)
          color3.insert(_index,_color)
         
          _opacity = opacity3[_index]
          opacity3.pop(_index)
          opacity3.insert(_index,_opacity)

          _size = size3[_index] +5
          size3.pop(_index)
          size3.insert(_index,_size)
    #[END]
    else:
        x3.append(2)
        y3.append(now)
        text3.append(_text)
        color3.append(_color)
        opacity3.append(_opacity)
        size3.append(_size)


trace_red3 = go.Scatter(
        x=x3,
        y=y3,
        mode='markers',
 
        #制订每个点,对应的悬浮文字提示信息(<br>标识换行);
        #text=['第1个气泡<br>size: 40<br>这里可以填写内容', '第2个气泡<br>size: 60', '第3个气泡<br>size: 80', '第4个气泡<br>size: 100'],
        text=text3,
        marker=dict(
        #指定每个点的颜色
        color=color3,
        #指定每个点的透明度
        opacity=opacity3,
        #指定每个点的大小
        size=size3,
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
 
data = [trace_red0,trace_red2,trace_red3]
pyplt(data, filename='./1.html')



