# Mapping earthquakes in Python 3.5 using [Plotly](https://plot.ly/)
### Wrangling work with earthquake dataset.


Here's my output: 8hrs of hardwork

[![quack 1.png](https://s19.postimg.org/51ecmf86r/quack_1.png)](https://postimg.org/image/ow0e8jne7/)




## Download the USGS quakes data

The USGS earthquakes dataset, download it from [Earthquake Hazards Program](http://earthquake.usgs.gov/earthquakes/feed/v1.0/csv.php):
http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.csv



## Setting data on Map
```
cases = []
for i in range(len(types)):
    lim = types[i]
    df_sub = df.loc[df.type==types[i],:]
    cases.append(go.Scattergeo(
        lon = df_sub['longitude'],
        lat = df_sub['latitude'],
        text = df_sub['text'],
        #colorscale = scl,
        #autocolorscale = False,
        name = types[i] + ' : '+str(len((df_sub))),
        marker = dict(
            line = dict (color = colors[i],width = 0.5),
            #sizemode = 'area',
            size = types[i]
            #size = len(df_sub)/8324
```
## Legend dataset
```
data1=df.groupby('type').count()
```
[![screenshot_1.png](https://s19.postimg.org/gww1dh8ab/screenshot_1.png)](https://postimg.org/image/aj6ya83e7/)

