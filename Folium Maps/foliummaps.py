# Auto detect text files and perform LF normalization
* text=auto
import folium
import pandas
map=folium.Map(location=[88,-180])
fgv=folium.FeatureGroup(name="VOLCANOES")
fgp=folium.FeatureGroup(name="POPULATION")
data=pandas.read_csv("VOLCANOES.txt")
lat=list(data["LAT"])
lon=list(data["LON"])
el=list(data["ELEV"])
for lt,ln,e in zip(lat,lon,el):
    fgv.add_child(folium.CircleMarker(location=[lt,ln],popup=str(e),radius=7,fill_color=' blue',color='green',fill_opacity=0.8))

map.add_child(fgv)
fgp.add_child(folium.GeoJson(data=open("world.json",'r',encoding='utf-8-sig').read(),style_function=lambda x:{'fillColor' :'yellow' if x['properties']['POP2005']>10000000 else 'orange' if x['properties']['POP2005']>50000000 else 'red'}))
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("MAPS.html")
