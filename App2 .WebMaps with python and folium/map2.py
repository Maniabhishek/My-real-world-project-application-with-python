import folium
import pandas
data=pandas.read_csv("Volcanoes.txt")
lat=list(data["LAT"])
lon=list(data["LON"])
elev=list(data["ELEV"])

map=folium.Map(location=[38.58,-99.09],zoom_start=6,tiles="Mapbox Bright")

def color_producer(elevation):
    if elevation<1000:
        return "green"
    elif 1000<=elevation<3000:
        return "orange"
    else:
        return "red"

fgv=folium.FeatureGroup("Volcanoes")
for lt,ln,el in zip(lat,lon,elev):
    fgv.add_child(folium.CircleMarker(location=[lt,ln],popup=str(el)+"m",radius=6,
    fill_color=color_producer(el),color="grey",fill=True,fill_opacity=0.7))
fgp=folium.FeatureGroup("populaation")

fgp.add_child(folium.GeoJson(data=open('world.json','r',encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005']<1000000 else 'orange'
if 1000000<=x['properties']['POP2005']<20000000 else "red"}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("Map2.html")
