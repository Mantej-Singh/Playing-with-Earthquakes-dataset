#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df=pd.read_csv('All Earthquakes.csv')


# In[3]:


df.head()


# In[4]:


df['time']=pd.to_datetime(df['time'])


# In[5]:


df.head()


# In[6]:


df['Year_month']=df['time'].apply(lambda x: x.strftime('%b-%y')) 


# In[7]:


data1=df.groupby('type').count()


# In[8]:


data1=data1.reset_index()


# In[9]:


data1.head()


# In[10]:


data1=data1[['type','time']]


# ### rename the colum

# In[11]:


data1.columns.values[1]='count'


# In[12]:


data1


# In[13]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[14]:


data1.plot(kind='bar',subplots=True,)


# # Plotting using Plotly API

# In[15]:


import plotly 
import chart_studio.plotly as py
import plotly.graph_objs as go
#Setting plotly credentials
py.sign_in('username','key')


# In[16]:


data = [go.Scatter(
        x=data1['type'],
        y=data1['count'],
        name = 'lines+markers'
           
    )
       
       ]
layout = go.Layout(
title='<b>Number Of Calamities</b>',
xaxis=dict(title='Type',color = ('Black')),
yaxis=dict(title='Counts',color = ('Black'))
)
fig = go.Figure(data=data, layout=layout)
py.iplot(fig,filename='Earthquakes')


# In[17]:


fig = go.Figure([go.Bar(x=data1['type'], y=data1['count'])])
py.iplot(fig,filename='Earthquakes')


# In[18]:


colors = ["rgb(0,116,217)","rgb(255,65,54)","rgb(133,20,75)","rgb(255,133,27)","lightgrey"]


# In[19]:


df['text'] = 'Type: '+df['type']  + '<br>' + 'Place: '+df['place']


# In[20]:


types = data1['type'].tolist()
len(types)


# #### i was trying with mpl Basemap but could not import the package, then i tried with plotly

# In[21]:


import importlib
importlib.import_module('mpl_toolkits').__path__


# In[22]:


#from mpl_toolkits.basemap import Basemap


# ## New code:

# ## finding the latitudes  and longitudes by type

# In[23]:


for i in range(len(types)):
    #lim = types[i]
    df_sub = df.loc[df.type==types[i],:]
    print(len(df_sub))


# In[ ]:


for i in range(len(types)):
    print(types[i])


# In[25]:




cases = []
for i in range(len(types)):
    lim = types[i]
    df_sub = df.loc[df.type==types[i],:]
    cases.append(go.Scattergeo(
        lon = df_sub['longitude'],
        lat = df_sub['latitude'],
        text = df_sub['text'],
        name = types[i] + ' : '+str(len((df_sub))),
        marker = go.scattergeo.Marker(
            color = colors[i],
            sizemode = 'area'
                )
    ) )


# In[26]:



layout = dict(
    title = '<b>Most Calamities</b>  <br>(Hover for details)',
    #colorbar = True,
    showlegend = True,
    geo = go.layout.Geo(
    showframe = False,
    showcoastlines = True,
    showcountries = True,
    showland = True,
    landcolor = 'rgb(217, 217, 217)',
    subunitwidth=1,
    countrywidth=1,
    subunitcolor="rgb(255, 255, 255)",
    countrycolor="rgb(255, 255, 255)"
    
    ),
)

fig = go.Figure( data=cases, layout=layout )
py.iplot( fig, validate=False, filename='Eqack 1', fileopt='overwrite' )


# # Update(Oct 8): Updated the code with latest plot.ly references. Thanks to Mai (@maihao14) for pointing out the issue

# In[ ]:




