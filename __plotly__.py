
#!/usr/bin/env python
# coding:utf-8

#***************************************************
# * Author         :  ZangDezhi
# * Email          :  winzdz@hotmail.com
# * Create Time    : 2020-01-07 20:21
# Last Modified  : 2020-01-08 17:20:19
# * FileName       : __plotly__.py
#**************************************************
import plotly.express as px

df = px.data.gapminder().query("country=='Canada'")
fig = px.line(df, x="year", y="lifeExp", title='Life expectancy in Canada')
fig.show()
