#%% Import packages
from pyleaf import  addGeoJSONPolygon, geoSearch, addPopupButton, layerControl, makeMap, addTile, fullScreen, load_data, geojsonOpts, newLayer, layerSearch, insertLegend, addHeat
import pandas as pd 
import re
import geopandas as gpd
#import datetime as dt


#%% Dictionaries
vehicle_type_simplification = {
"Bus or Motor Stage": "Bus",
"Farm Tractor and/or Farm equipment": "Tractor",
"Moped": "Moped",
"Motorcycle": "Motorcycle",
"Neighborhood Electronic Vehicle": "Other",
"Not Stated": "Other",
"Other": "Other",
"Passenger Car": "Car",
"Pickup,Panel Truck or Vanette under 10,000 lb": "Truck-pickup",
"Railway Vehicle": "Train",
"School Bus": "Bus",
"Scooter Bike":"Moped",
"Taxi": "Taxi",
"Truck & Trailer": "Truck",
"Truck (Flatbad,Van,etc)": "Truck-pickup",
"Truck - Double Trailer Combinations": "Truck",
"Truck Tractor": "Truck",
"Truck Tractor & Semi-Trailer": "Truck"
}


vehicle_type_extra_simple = {
"Bus or Motor Stage": "Large",
"Farm Tractor and/or Farm equipment": "Large",
"Moped": "Motorcycle",
"Motorcycle": "Motorcycle",
"Neighborhood Electronic Vehicle": "Other",
"Not Stated": "Other",
"Other": "Other",
"Passenger Car": "Car",
"Pickup,Panel Truck or Vanette under 10,000 lb": "Truck",
"Railway Vehicle": "Other",
"School Bus": "Large",
"Scooter Bike":"Motorcycle",
"Taxi": "Car",
"Truck & Trailer": "Large",
"Truck (Flatbad,Van,etc)": "Truck",
"Truck - Double Trailer Combinations": "Large",
"Truck Tractor": "Large",
"Truck Tractor & Semi-Trailer": "Large"
}


#%% Load and prepare the data #################################################








# Create the pandas DataFrames
df = pd.DataFrame([[-1,'Mohammed', 22, 'School Bus', 'Possible Injury', 47.2, -123.2, 2, '11/01/2019 01:30:00.000',0],[0,'Steven', 39, 'Truck (Flatbad,Van,etc)', 'Possible Injury', 47.1, -123, 8, '11/01/2021 01:30:00.000',1],[1,'Josh', 41, 'Truck Tractor', 'Possible Injury', 47.037872, -122.900696, 1, '10/31/2021 01:30:00.000',1], [2,'robert', 20, 'Motorcycle', 'No Injury', 46.023064, -123.176483, 1, '10/31/2021 01:30:00.000',1],[3,'jacob', 20, 'Motorcycle', 'No Injury', 45.523064, -122.676483, 2, '10/31/2021 01:30:00.000',0], [4,'nick', 25, 'Passenger Car', 'Serious Injury',  47.171764, -122.518456, 3, '05/29/1986 01:30:00.000',0], [5,'juli', 24, 'Passenger Car', 'Fatal',  47.258728, -122.465973, 4, '11/01/1982 01:30:00.000',0]], columns=['Report Number','Name', 'Age', 'Vehicle Type', 'Severity', 'Latitude', 'Longitude', 'Number of Vehicles Involved', 'Date', 'MCEndorsed'])




travel = pd.DataFrame([
    [0, "Charleston International Airport", "2022-10-26 15:59:00", 32.8925, -80.0377, "", "plane", "travel", 'blue']   
    ], columns = ["ID", "Location", "Date", "Latitude", "Longitude", "Popup", "icon", "Type", "color"])



events = pd.DataFrame([
    [0, "Williams-Brice Stadium", "2022-10-29 08:00:00", 33.9705, -81.0182, "Time is a placeholder -- game time is not set.", "calendar", "event", 'red']
    ], columns = ["ID", "Location", "Date", "Latitude", "Longitude", "Popup", "icon", "Type", "color"])



restaurants = pd.DataFrame([
    [0, "Pomegranate on Main", "2022-11-04 19:00:00", 34.84495 ,-82.402718, "We should reserve a table. Need to wait within 30 days.", "utensils", "restaurant", 'green']
    ,[1, "Hyman's Seafood", "2022-10-27 11:00:00", 32.78174 ,-79.931656, "No reservations.", "fish", "restaurant", 'green']
    ], columns = ["ID", "Location", "Date", "Latitude", "Longitude", "Popup", "icon", "Type", "color"])










# =============================================================================
# # Add a column for color of the marker 
# # List of available colors: https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.css
# df.loc[df['Severity'] == 'No Injury', 'color'] = 'lightblue'
# df.loc[df['Severity'] == 'Serious Injury', 'color'] = 'orange'
# df.loc[df['Severity'] == 'Possible Injury', 'color'] = 'orange'
# df.loc[df['Severity'] == 'Fatal', 'color'] = 'red'
# 
# # Use the simplified data from the vehicle type dictionary to find a 'font-awesome' icon for each crash
# df['icon']=df['Vehicle Type'].map(vehicle_type_simplification)
# df['Type']=df['Vehicle Type'].map(vehicle_type_extra_simple)
# 
# #Create additional classes to add based on endorsement, and the number of vehicles in a crash
# df['single']=''
# df['single'][df['Number of Vehicles Involved']==1] = 'singleVehicle'
# 
# df['multi'] = ''
# df['multi'][df['Number of Vehicles Involved']>1] = 'multiVehicle'
# 
# df['mc_endorsed'] = ''
# df['mc_endorsed'][df['MCEndorsed']==1] = 'mcEndorsement'
# 
# =============================================================================




#%%Test the code#################################################################
 #Create the map and basic functions
 #Note: Obviously the layers in this code haven't been created yet. That is fine. This is done first because it also initializes the template. 
SC_Trip = makeMap(Longitude=-80.925, Latitude=33.836944, startZoom=7.5,default_layers="osm, travel, events, restaurants, cities" ,maptitle='Pettis Family South Carolina Trip - 2022')
SC_Trip = addTile(SC_Trip) #Adds open street map basemap 

#Load data
SC_Trip = load_data(mapname=SC_Trip, dataframe=travel, id='ID', dataname = 'travel_data') #Loads the given df and converts to GeoJSON
SC_Trip = load_data(mapname=SC_Trip, dataframe=restaurants, id='ID', dataname = 'restaurants_data') #Loads the given df and converts to GeoJSON
SC_Trip = load_data(mapname=SC_Trip, dataframe=events, id='ID', dataname = 'events_data') #Loads the given df and converts to GeoJSON


#Create a new layer with the above options 

#Commenting this out. Is this needed??
SC_Trip = newLayer(SC_Trip, 'travel', dataname = 'travel_data')
SC_Trip = newLayer(SC_Trip, 'events', dataname = 'events_data')
SC_Trip = newLayer(SC_Trip, 'restaurants', dataname = 'restaurants_data')



#Some templates for the GeoJSON Options program
#First, define the appearance of the popups
#mypopup = """'<table class="popup-table"> <tr>  <th>Age</th>  <th>Severity</th>  <th>Date</th>  </tr>  <tr> <td>{}</td>  <td>{}</td> <td>{}</td>  </tr></table>'.format(feature.properties.Age, feature.properties.Severity, feature.properties.Date)"""
#mypopup = "feature.properties.Type+'<br><b>'+feature.properties.Name+'</b>'"
#mypopup = """`
# <table class='popup-table'>   
#     <tr>
#         <th>Age</th>
#         <th>Severity</th>
#         <th>Date</th>
#     </tr>
#     <tr>
#         <td>data[i].Age</td>
#         <td>data[i].Severity</td>
#         <td>data[i].Date</td>
#     </tr>
# </table>
# `;
# """

mypopup = """'

<div id="card-stack-content" class="card-stack-content">
	<ul>
		<li class="event-card selected">
			<div class="card-row">
				<span>
					<div class="card-cell">
						<h4>Date</h4>{}
					</div>
				</span>
				<span>
					<div class="card-cell">
						<h4>Location</h4>{}
					</div>
				</span>
				<span>
					<div class="card-cell">
						<h4>Notes</h4>{}
					</div>
				</span>
			</div>
		</li>
	</ul>
</div>
    
'.format(feature.properties.Date, feature.properties.Location, feature.properties.Popup)"""
mypopup = re.sub('\n',' ',mypopup).strip() # remove line breaks

#What should the icon of the marker be?
myicon = """'<i class ="fa-rotate-0 fa fa-{} icon-white"></i>'.format(feature.properties.icon.toLowerCase())"""

#What variable should define a new class that gets added to the marker element?
myclass = "Type"

#Some more classes that may be required
#Adding required classes for the font-awesome icons,
#for fixing some formatting issues, and classes for the extra options (single/multi vehicle and if they have a mc endorsement)
myextraclasses = "' awesome-marker-icon-{}  awesome-marker mydiv {} {} {}'.format(feature.properties.color)"


#Creates a new layer from the loaded geoJSON layer
SC_Trip = geojsonOpts(mapname=SC_Trip, classname=myclass, extraclasses=myextraclasses, popup=mypopup, icon=myicon, dataname='travel_data', optionsname='geojsonOpts' )
SC_Trip = geojsonOpts(mapname=SC_Trip, classname=myclass, extraclasses=myextraclasses, popup=mypopup, icon=myicon, dataname='events_data', optionsname='geojsonOpts' )
SC_Trip = geojsonOpts(mapname=SC_Trip, classname=myclass, extraclasses=myextraclasses, popup=mypopup, icon=myicon, dataname='restaurants_data', optionsname='geojsonOpts' )



#Now, put together the layer control
baseMaps = """
    "OpenStreetMap": osm,
    "Mapbox Streets": streets,
    "Black and White" :Stamen_TonerLite
"""

overlayMaps = """
    "Travel Locations" : travel,
    "Events": events,
    "Restaurants": restaurants,  
    "Cities": cities
"""


#Adds layer control using the above options.
SC_Trip = layerControl(SC_Trip, baseMaps, overlayMaps)


#Adds a layer search control, with the third option being what you can search for
# and the fourth option being the variable in the dataset that will be returned.
# with 'Name', 'Type' we can search for a name and get back the type of vehicle with the link to the coordinates
SC_Trip = geoSearch(SC_Trip)
SC_Trip = fullScreen(SC_Trip) #Adds full screen button


#Insert legend
# List of icons: https://fontawesome.com/search?p=1&q=vehicle&s=solid%2Cbrands
# mylegend = '''
# <div style="
#     position: fixed; 
#     bottom: 50px;
#     left: 50px;
#     width: 250px;
#     height: 80px;
#     z-index:9999;
#     font-size:14px;
#     ">
#     <p><a style="background-color:lightblue;color:white;font-size:150%;margin-left:20px;"> <i class='fa fa-car' aria-hidden="true"></i></a>&emsp;No Injury</p>
#     <p><a style="background-color:orange;color:white;font-size:150%;margin-left:20px;"> <i class='fa fa-car' aria-hidden="true"></i></a>&emsp;Injury</p>
#     <p><a style="background-color:red;color:white;font-size:150%;margin-left:20px;z-index = 99999;"> <i class='fa fa-car' aria-hidden="true"></i></a>&emsp;Fatal</p>

# </div>
# <div style="
#     position: fixed; 
#     bottom: 50px;
#     left: 50px;
#     width: 120px;
#     height: 90px; 
#     z-index:9998;
#     font-size:14px;
#     background-color: #ffffff;
#     opacity: 0.65;
#     ">
# </div>
# '''    
    
# SC_Trip = insertLegend(SC_Trip,mylegend)


#Load in a multipolygon (like counties)
"""I believe the easiest way to add/change geoJSON data in our context
is to load in a geoJSON and convert to a geodataframe, manipulate it, 
and return to geoJSON.

GeoPandas will help us accomplish this. 
"""
#SC Cities
cities = gpd.read_file('tl_2017_45_cousub.shp')
#Now add fill colors
cities['fillColor'] ='#00ff00'
#mygeodataframe.loc[mygeodataframe.name=='Pierce', 'fillColor'] ='#0000ff'
#mygeodataframe.loc[mygeodataframe.name!='Pierce', 'fillColor'] ='#00ff00'

#Fill Opacity
cities['fillOpacity'] = 0.15

#Weights 
cities['weight']=2

#color
cities['color']='#000080'

#opacity 
cities['opacity'] = 1

#Make proper case
cities['NAME']= cities['NAME'].str.title()

#Should this polygon get shown?
cities['show_on_map'] = "false"
cities.loc[cities.NAME=='Greenville', 'show_on_map'] = "true"
cities.loc[cities.NAME=='Camden', 'show_on_map'] = "true"
cities.loc[cities.NAME=='Columbia', 'show_on_map'] = "true"
cities.loc[cities.NAME=='Charleston Central', 'show_on_map'] = "true"
cities.loc[cities.NAME=='West Columbia-Cayce', 'show_on_map'] = "true"
cities.loc[cities.NAME=='Myrtle Beach', 'show_on_map'] = "true"
cities.loc[cities.NAME=='North Charleston', 'show_on_map'] = "true"
cities.loc[cities.NAME=='Camden Northeast', 'show_on_map'] = "true"



#Cutting out cities I am not using, to troubleshoot why these aren't showing up.
cities = cities[cities['show_on_map']=="true"]

#Add county polygon
SC_Trip = addGeoJSONPolygon(mapname=SC_Trip, geodataframe=cities, geojsonname='cities',popup='NAME')
















#Save the file 
with open("sc_trip.html", "w") as file:
    file.write(SC_Trip)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    