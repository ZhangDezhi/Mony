
#!/usr/bin/env python
# -!- coding: utf-8 -!-

#***************************************************
# * Author         :  ZangDezhi
# * Email          :  winzdz@hotmail.com
# * Create Time    : 2020-01-09 15:55
# Last Modified  : 2020-01-09 15:56:11
# * FileName       : __plotly__.py
#**************************************************


import plotly.graph_objects as go
fig = go.Figure(data=go.Bar(y=[2, 3, 1]))
fig.show()


