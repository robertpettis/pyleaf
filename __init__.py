import strings
import re 
import json
import geojson
import pandas as pd 
#from geojson import Feature, FeatureCollection, Point
from datetime import datetime

__version__ = '1.0'

#Future Updates:
    #Custom icon in layer control:
        #https://plnkr.co/edit/Se17LxLjqGg6sJTYNCoq?p=preview&preview
    #Font awesome markers:
        #https://stackoverflow.com/questions/66590403/leaflet-search-custom-result-marker
    #Save search result in leaflet
        #https://stackoverflow.com/questions/56483297/how-to-reuse-search-result-in-leaflet-control-search



#Creates the map HTML framework ###############################################
def makeMap(Longitude, Latitude, startZoom, default_layers="osm", maptitle='Quick Start - Leaflet', attributioncontrol = 'false'):
    map_object = strings.map_string
    map_object = re.sub(r'\/\/Make map #*\s{2}',f'''//Make map ##################################################################
var map = L.map('map', {{
    attributionControl: {attributioncontrol},
    center: [{Latitude}, {Longitude}],
    zoom: {startZoom},
    layers: [{default_layers}]
}});
                        

''',map_object)                        

    #Changes page title
    if maptitle!='Quick Start - Leaflet':
        map_object = re.sub('Quick Start - Leaflet',maptitle, map_object)
        
    return map_object 

#testing the package ######################################################
def my_pip_package():
	print("It's working!")

#Adds full screen option ######################################################
def fullScreen(mapname) :
    map_object = mapname
    map_object = re.sub(r'\/\/Other Options #*\s{2}',f'''//Other Options ##################################################################

//Full Screen
map.addControl(new L.Control.Fullscreen());

''',map_object)

    return map_object 



#Adds basemap #################################################################
#Future update is to add complete functionality. Right now, just loading common ones by name is good enough.
def addTile(mapname, tilename = 'openstreetmap'):
    map_object = mapname
    if tilename == 'openstreetmap':
        map_object = re.sub(r'\/\/Add tiles #*\s{,2}',f'''//Add tiles #################################################################

{strings.tiles}

''', map_object)
    return map_object



def layerControl(mapname, base, overlay):
    map_object = mapname 

    control_list = f"""
var baseMaps = {{
{base}    
}};    

var overlayMaps = {{
{overlay}
}};



var layerControl = L.control.layers(baseMaps, overlayMaps).addTo(map);
"""

    map_object = re.sub(r'\/\/Layer control #*\s{,2}',f'''//Layer control #################################################################

{control_list}

''', map_object)
    return map_object
    






#load data#####################################################################
def load_data(mapname, dataframe, id,  dataname = 'data', lat='Latitude', lon = 'Longitude'):
    map_object=mapname
    data_object = dataframe    
    coords = data_object[[lat, lon]]    
    non_coords = data_object.drop(columns=[lat,lon])

    geoJSONinnards  = ""
    for idx, val in enumerate(non_coords.iloc[:, 0]): #For each row
        geometry = ""
        properties = ""
        colnum = 0
        for col in non_coords:         #for each column
            colnum+=1            
            #Remove final comma########### 
            if colnum==non_coords.shape[1]:
                comma = ""
            else:
                comma = ","
            ###############################    
            properties += """      "{}": "{}"{}            
""".format(col, non_coords[col][idx], comma)
              
        geometry = """
   "geometry": {{
      "type": "Point",
      "coordinates": [
         {},
         {}
      ]
   }}                   
""".format(coords[lon][idx], coords[lat][idx]) #GeoJSON uses lng-lat 
                    


        #Remove final comma###########
        if len(data_object)==idx+1:
            comma = ""
        else:
            comma =","
        ##############################
        geoJSONinnards +="""
{{
   "type": "Feature",
   "id": "{}",
   "properties":{{
""".format(data_object[id][idx]) + properties  + "}, "  + geometry + "}}{}".format(comma)


    now = datetime.now()
    name = data_object.attrs.get('name')
    outer = f"""var {dataname} = {{
   "type": "FeatureCollection",
   "generator": "overpass-turbo",
   "References": "These data were produced by the Washington State Department of Licensing, the Washington State Department of Transportation, and the Washington Traffic Safety Commission Coded Fatal Collision Data.",
   "timestamp": "{now}",
   "features": [{geoJSONinnards}
  ]
}};
"""

    #Insert the string into the html                        
    map_object = re.sub(r'\/\/Data #*\s{,2}',f'''//Data #################################################################

{outer}''', map_object)  

    return map_object
    
  



#the icon part is temporary and will be changed ASAP
#Add functionality to put multiple datasets into a single layer
#Convert the imported GeoJSON to 
def geojsonOpts(mapname, classname, extraclasses, popup, icon=None, dataname = 'data', optionsname ='geojsonOpts'):
    map_object = mapname

    if icon!=None:
        string_object = f"""
var	{optionsname} = {{
 			pointToLayer: function(feature, latlng) {{
				return L.marker(latlng, {{
 					icon: L.divIcon({{
						className: feature.properties.{classname} + {extraclasses},
						iconSize: L.point(16, 16),
						html: {icon},
 					}})
				}}).bindPopup({popup});
 			}}
		}};


"""

    else: 
        string_object = f"""
var	{optionsname} = {{
 			pointToLayer: function(feature, latlng) {{
				return L.marker(latlng, {{
 					icon: L.AwesomeMarkers.icon({{
                         extraClasses: "fa-rotate-0 dummy", 
                         icon: "motorcycle", 
                         iconColor: "white", 
                         markerColor: "orange", 
                         prefix: "fa"
                         }})
				}}).bindPopup({popup});
 			}}
		}};


"""      




    map_object = re.sub(r'\/\/GeoJSON Options #*\s\s',f'''//GeoJSON Options  #################################################################

{string_object}

''', map_object)   



    return map_object 






#Create new layers ############################################################
def newLayer(mapname, layername, dataname = 'data', optionsname ='geojsonOpts', addToMap=False):
    map_object = mapname
    
    #Adding directly to the map is not the default because of the possibility of adding to a layer and therefore layer control
    #If the addToMap option is True, then this will allow it to be directly added
    mapadd = ''
    if addToMap==True:
        mapadd = '.addTo(map);'
    
    
    #Insert the string into the html                        
    map_object = re.sub(r'\/\/Make layers #*\s{,2}',f'''//Make layers #################################################################

var {layername} = L.layerGroup([
	L.geoJson({dataname}, {optionsname})
]){mapadd}

''', map_object)   
    
    return map_object



#Create a search bar for searching the layers 
#https://github.com/stefanocudini/leaflet-search
def layerSearch(mapname, layers ,searchvar, tooltipvar):
    map_object = mapname
    tip_var = tooltipvar.lower()
    
    if len(layers)==1:
        the_layer = layers[0]
        map_object = re.sub(r'\/\/Other Options #*\s{2}',f'''//Other Options ##################################################################

//Layer Search
L.control.search({{
	position:'topleft',		
	layer: {the_layer},
	initial: false,
	propertyName: '{searchvar}',
	buildTip: function(text, val) {{
		var {tip_var} = val.layer.feature.properties.{tooltipvar};
		return '<a href="#" class="'+{tip_var}+'">'+text+'<b>'+" "+{tip_var}+'</b></a>';
	}}
}})
.addTo(map);


''',map_object)
    
    if len(layers)>1:
        print("Feature coming soon.")

    return map_object     



def geoSearch(mapname):
    map_object = mapname

    string = """
// Other types of searches: https://opengeo.tech/maps/leaflet-search/
// This example, in particular, is quite informative on how to build a custom map 
// and how data, loops, etc. work in JS: 
// view-source:https://opengeo.tech/maps/leaflet-search/examples/simple.html
map.addControl(new L.Control.Search({
    url: 'https://nominatim.openstreetmap.org/search?format=json&q={s}',
    jsonpParam: 'json_callback',
    propertyName: 'display_name',
    propertyLoc: ['lat', 'lon'],
    marker: L.circleMarker([0, 0], {
        radius: 30
    }),
    autoCollapse: true,
    autoType: false,
    minLength: 2
}));
"""    
    map_object = re.sub(r'\/\/Other Options #*\s{2}',f'''//Other Options ##################################################################
{string}
''',map_object)
    return map_object
    
    
    




def insertLegend(mapname, legend):
    map_object = mapname
    map_object = re.sub('<div id="mapid"></div>',f'''
<div id="mapid"></div>

{legend}                        
                        
                        ''',map_object)
    
    
    return map_object 
    

    


#Heatmap#######################################################################
def addHeat(mapname, heatname, data, lat = 'Latitude', lon = 'Longitude', intensity = 1, radius = 25, blur=25, maxZoom=11, gradient = '.4:"blue",.6:"cyan",.7:"lime",.8:"yellow",1:"red"'):
    """ Some comments about the options from 'leaflet.js Essentials' by Paul Crickard:

Gradient: The gradient option allows you to specify the
color at different levels. The default is set to
{.4:"blue",.6:"cyan",.7:"lime",.8:"yellow
",1:"red"}. You can specify ranges from 0 to 1.
The outermost color is 0 and the center is 1. The
default setting tends to be a common color range
for heatmaps that most people understand.
Leaving the default is the best option, but if you
need to change the colors for some reason, you
can.    

Blur: Blur merges the points the together, or not. A low
blur value will create individual points, whereas a
higher number will make the points merge with
each other and look more fluid. Blur too much
and you will wash out your points...It will take
some to adjust to finding the perfect value.
Starting with the default value of 15 is a good
idea


"""


    map_object = mapname
    df = data
    if type(intensity)==int:
        print("Type is 'int.'")
        print("Functionality coming 'soon.'")        

    elif type(intensity)==str:
        
        #Create heat data
        heat_df = df[[lat, lon, intensity]]
        heat_df = heat_df.to_records(index=False)
    
        heat = ""
        for idx, val in enumerate(heat_df):
            if idx < len(heat_df)-1:
                heat += str(val) + """,
        """
            if idx == len(heat_df)-1:
                heat+=str(val)
        heat = re.sub('\(','   [', heat)        
        heat = re.sub('\)',']', heat)        
        heat = f"""var {heatname} = L.heatLayer([  
   // [lat, lng, intensity]        
{heat}  
], {{radius: {radius}, blur: {blur}, maxZoom: {maxZoom}, gradient: {{{gradient}}}}})
                        
"""              
        map_object = re.sub(r'\/\/Heat Maps #*\s{,2}',f"""//Heat Maps ###################################################################
{heat}

""",map_object)
        return map_object        
        print("Heat map added.")
    else:
        raise Exception("Data type for 'intensity' must be an integer or a string (column name).")






def addPopupButton(mapname, icon, template, bheight = '26px', bwidth='26px', hover = 'hover text', buttonid='YOUR-BUTTON-ID', classes='legend-popup'):
    map_object = mapname 

    thestring = """
    
//Draggable popups
function makeDraggable(popup){
  var pos = map.latLngToLayerPoint(popup.getLatLng());
  L.DomUtil.setPosition(popup._wrapper.parentNode, pos);
  var draggable = new L.Draggable(popup._container, popup._wrapper);
  draggable.enable();
  
  draggable.on('dragend', function() {
    var pos = map.layerPointToLatLng(this._newPos);
    popup.setLatLng(pos);
  });
}


"""    
    
    map_object = re.sub(r'\/\/Custom Functions #*\s{,2}',f"""//Custom Functions ###################################################################
{thestring}

""",map_object)    
    


    secondString = f"""
    
var legend_lat =  map.getBounds().getCenter().lat   
var legend_lon = map.getBounds().getCenter().lng
var legend_latlon = [legend_lat, legend_lon]        
    
    
    
L.easyButton('{icon}', function(event) {{
    var thepop = L.popup({{className: '{classes}'}})
    .setLatLng(legend_latlon)
    .setContent('{template}')
    .openOn(map);
    makeDraggable(thepop);
}}, '{hover}', '{buttonid}').addTo(map);
"""


    map_object = re.sub(r'\/\/Icon Legend #*\s{,2}',f"""//Icon Legend ###################################################################
{secondString}

""",map_object)    




    the_css = f"""
#{buttonid} {{
  height: {bheight}; 
  width: {bwidth};  
}}
"""


    map_object = re.sub(r'\/\*Legend Button Reserved Space\*\/',f"""/*Legend Button Reserved Space*/
{the_css}
""",map_object)   







    return map_object











#Create a GeoJSON formatted object which includes style and if they should be filtered. 
#The input data should be a GeoDataframe (geopandas)
def addGeoJSONPolygon(mapname, geodataframe, geojsonname, fillColor='fillColor', weight='weight', opacity='opacity', color='color', fillOpacity='fillOpacity', show='show_on_map', popup='popupContent'):
    #I need to work a bit here and there with both the geodataframe and the geojson to make this work how I envision it.
    mygeodataframe = geodataframe    
    mygeojson =  mygeodataframe.to_json()
    map_object = mapname
    #Now, create a list of all properties and geometries in the GeoJSON 
    properties = pd.DataFrame(re.findall(r'\"properties\": \{.+?\}',mygeojson), columns={'Results'})
    geometries = pd.DataFrame(re.findall(r'\"geometry\": \{.+?\}',mygeojson), columns={'Results'})
    assert len(properties)==len(geometries) #making sure I got one of each 

    #Now, create the style property
    innards = ''
    for idx, val in enumerate(properties['Results']):
        styleweight = mygeodataframe.loc[mygeodataframe.index[idx], weight]
        stylecolor = mygeodataframe.loc[mygeodataframe.index[idx], color]      
        styleopacity = mygeodataframe.loc[mygeodataframe.index[idx], opacity]        
        stylefillColor = mygeodataframe.loc[mygeodataframe.index[idx], fillColor]       
        stylefillOpacity = mygeodataframe.loc[mygeodataframe.index[idx], fillOpacity]        

        polygon_popup = mygeodataframe.loc[mygeodataframe.index[idx], popup]
        
        add_string = f"""
"style": {{
      "weight": {styleweight},
      "color": "{stylecolor}",
      "opacity": {styleopacity},
      "fillColor": "{stylefillColor}",
      "fillOpacity": {stylefillOpacity}
  }},     
"""
        #Now, use re sub to insert the string above into the properties.
        properties.iat[idx,0] = re.sub(r"\"properties\": {",f"\"properties\": {{ {add_string} ",properties.iat[idx,0])

        #Make sure commas don't show up when they aren't supposed to.
        #First, find length of the data (we asserted them both be the same earlier, so one will do)
        if idx +1 == len(properties):
            comma = ""
        else:
            comma = ", "
        
        
        #Add everything back together
        innards +=f"""{{
    "id": {idx}, 
    "type": "Feature",
""" + properties.iat[idx,0] + ", " + geometries.iat[idx,0]+"""
}"""  + comma + """
"""

    outer = f"""var {geojsonname}_data = {{"type":"FeatureCollection","features":[
""" + innards + """
]};"""    


    map_object = re.sub(r'\/\/Data #*\s{,2}',f'''//Data #################################################################

    {outer}

''', map_object)        
    
    #Now that the data is included, we need to include a function to add the polygon to the map. 

    add_to_map = 	f"""
    var {geojsonname} = L.layerGroup([L.geoJSON({geojsonname}_data, {{
      filter: function(feature, layer) {{
          return feature.properties.{show};    
      }},
    
    	style: function (feature) {{
    		return feature.properties && feature.properties.style;
    	}},
    
    	onEachFeature: onEachFeature
    
    //	pointToLayer: function (feature, latlng) {{
    //		return L.circleMarker(latlng, {{
    //			radius: 8,
    //			fillColor: '#ff7800',
    //			color: '#000',
    //			weight: 1,
    //			opacity: 1,
    //			fillOpacity: 0.8
    //		}});
    //	}}
    }})
]) 
"""    
    
    map_object = re.sub(r'\/\/Add MultiPolygons #*\s{,2}',f'''//Add MultiPolygons #################################################################

    {add_to_map}''', map_object)            
    
    
    
    return map_object 

    



















