# -*- coding: utf-8 -*-
"""
Created on Thu Jul  7 15:18:46 2022

@author: RPettis240
"""

map_string = """

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    
    <title>Pettis Family SC Trip - 2022</title>
    
    <link rel="stylesheet" href="https://unpkg.com/leaflet@1.8.0/dist/leaflet.css" integrity="sha512-hoalWLoI8r4UszCkZ5kL8vayOGVae1oxXe/2A4AO6J9+580uKHDO3JdHb7NzwwzK5xr/Fs0W40kiNHxM9vyTtQ==" crossorigin="" />
    <script src="https://unpkg.com/leaflet@1.8.0/dist/leaflet.js" integrity="sha512-BB3hKbKWOc9Ez/TAwyWxNXeoV9c1v6FIeYiBieIWkpLjauysF18NzgR1MBNBXf8/KABdlkX68nAhlwcDFLGPCQ==" crossorigin=""></script>
    
    <script src='https://api.mapbox.com/mapbox.js/plugins/leaflet-fullscreen/v1.0.1/Leaflet.fullscreen.min.js'></script>
    <link href='https://api.mapbox.com/mapbox.js/plugins/leaflet-fullscreen/v1.0.1/leaflet.fullscreen.css' rel='stylesheet' />
    
    <script src='https://opengeo.tech/maps/leaflet-search/src/leaflet-search.js'></script>
    <link href='https://cdn.jsdelivr.net/npm/leaflet-search@2.9.7/dist/leaflet-search.min.css' rel='stylesheet' />
       
    
    	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.6.3/css/font-awesome.min.css"/>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.css"/>   
    <link rel="stylesheet" type="text/css" href="https://use.fontawesome.com/releases/v5.4.1/css/all.css">
    
    <script src="http://leaflet.github.io/Leaflet.heat/dist/leaflet-heat.js"></script>
    
    <script src="https://cdn.jsdelivr.net/npm/leaflet-easybutton@2/src/easy-button.js"></script>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/leaflet-easybutton@2/src/easy-button.css"/>
    
    
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/leaflet.draw/1.0.4/leaflet.draw.css"/>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/leaflet.draw/1.0.4/leaflet.draw.js"></script>

  
    
    
    

    <style>
        /*https://unpkg.com/leaflet@1.8.0/dist/leaflet.css is the leaflet.css file*/
        
        html,
        body {
            height: 100%;
            margin: 0;
        }
        
        .leaflet-container {
            left: 1%;
            height: 95%;
            width: 99%;
            max-width: 100%;
            max-height: 100%;
        }
        
        .hide {
            display: none;
        }
        
        #header {
            height: 90px;
            background-color: '#041E42'
        }
        
        #sitelogo {
            top: 10%;
            float: left;
            height: 75px;
            position: relative
        }
        
        #sitelogo img {
            height: 100%;
            position: relative
        }
        
        #checkboxes label {
            float: left;
        }
        
        #checkboxes ul {
            margin: 0;
            list-style: none;
            float: left;
        }
        
        .rightList {
            margin: 1%;
            float: right;
            text-align: left;
        }
        
        #iframe {
            width: 200px;
            height: 200px;
        }
        
      /*  .leaflet-container {
            z-index: 1;
        }    */
       

	   /* Just an example of how you can change the CSS of the map. This would turn the zoom buttons red. 
    .leaflet-bar > a:link { 
        color: red; 
        }
    */
        
        .leaflet-bottom {
            padding: 0px 10px;
            background: rgba(0, 0, 0, 0.5);
            color: #fff;
            font-size: 11px;
            line-height: 18px;
            border-radius: 5px;
        }
        
        p {
            margin: 0;
        }
		

	.mydiv {
	width: 35px !important; 
	height: 45px !important;
	}


.leaflet-control-layers-toggle:after{ 
    content:"Layers"; 
    color:black ;
}

.leaflet-control-layers-toggle{ 
    width:auto;
    background-position:2px 50% ;
    padding:2px;
    padding-left:36px;
    text-decoration:none;
    line-height:36px;

}

table {
  border-collapse: collapse;
}

th, td {
  border: 1px solid black;
}

.card-stack{
    position:absolute;
    top:2px;
    padding-top:38px;
    right:2px;
    max-height:calc(100% - 190px);
    height:auto;
    width:500px;
    overflow-y:scroll;
    box-shadow:0 19px 38px rgba(0,0,0,.3),0 15px 12px rgba(0,0,0,.22);
    z-index:10;
    color:#fff;
    overflow-x:hidden;
    overflow-y:auto;
    max-width:100vw
}
.card-stack.narrative-mode{
    right:2px;
    left:auto;
    top:237px;
    height:calc(100% - 487px)
}
.card-stack.full-height{
    max-height:calc(100% - 20px)
}
.card-stack .card-stack-header{
    position:fixed;
    top:2px;
    min-height:38px;
    line-height:38px;
    width:100%;
    max-width:500px;
    box-sizing:border-box;
    padding:0 5px;
    background:#000;
    border-radius:2px;
    border:1px solid #000;
    font-size:14px;
    transition:.2s ease;
    text-align:left;
    z-index:20
}
.card-stack .card-stack-header:hover{
    transition:.2s ease
}
.card-stack .card-stack-header .header-copy{
    margin:0;
    padding:0 5px;
    line-height:20px;
    text-align:right
}
.card-stack .card-stack-header .header-copy.top{
    padding-top:5px
}
.card-stack .card-stack-header .header-copy:last-child{
    padding-bottom:5px
}
.card-stack .card-stack-header .side-menu-burg{
    position:absolute;
    left:8px;
    top:9px
}
.card-stack .card-stack-header .side-menu-burg span{
    width:20px
}
.card-stack .card-stack-content{
    width:100%;
    max-width:500px;
}
.card-stack-content{
    font-family: "GT-Zirkon","Lato",Helvetica,sans-serif;  
    background: #efefef;
    }
.card-stack .card-stack-content ul{
    padding:0;
    margin-top:1px;
    margin-bottom:0
}
.card-stack .card-stack-content .card-list{
    height:auto
}
.card-stack.folded .card-stack-header{
    border:0;
    height:0;
    overflow:hidden
}
.card-stack.folded .card-stack-content{
    height:0;
    overflow:hidden
}

li{
    list-style-type:none
}


h4 {
    display: block;
    margin-block-start: 1.33em;
    margin-block-end: 1.33em;
    margin-inline-start: 0px;
    margin-inline-end: 0px;
    font-weight: bold;
}

.event-card h4 {
    margin-bottom: 0;
    margin-right: 5px;
    text-transform: uppercase;
    font-size: 11px;
    color: #7a7a7a;
    font-weight: 800;
}


.leaflet-popup-content-wrapper {
    padding: .25px !important;
    }


.leaflet-bottom.leaflet-right {
  max-width: 500px ~important;    
}



.legend-popup .leaflet-popup-tip {
    background: rgba(0, 0, 0, 0) !important;
    box-shadow: none !important;
}

.iconDetails {
 margin-left:1%;
float:left; 
height:40px;
width:60px;	
} 

.container2 {
	width:100%;
	height:auto;
	padding:1%;
}

h4 {
    margin:0px;
}

/*Legend Button Reserved Space*/




/*End legend button reserved space*/







    </style>


</head>

<body>

    <!--Header##################################################################-->
<!-- Header Menu of the Page -->
<header>
<div class='container2'>
		<div>
			<img src='http://www.signshopcolumbia.com/uploads/9/2/4/3/92435426/garnet-black-south-carolina-palmetto-flag-soda-city-sign-shop-columbia_orig.jpg' class='iconDetails'>
		</div>	
	<div style='margin-left:60px;'>
	<h4>Pettis Family SC Trip</h4>
	<div style="font-size:.6em;float:left;">10/2022 - 11/2022</div>
	</div>
</div>
</header>




    <div class="map-wrapper" tabindex="0" style="width: 99%; height: 92.5%;">
        <!--Map Div-->
        <div id="map">
        </div>

    </div>


<div id="mapid"></div>
   
  
</body>



<!--JavaScript##############################################################-->
<script>

//Data #####################################################################







//Custom Functions #########################################################


function zoomToFeature(e) {
	map.fitBounds(e.target.getBounds());
}   
    

//A function for adding popups to geoJSON 
function onEachFeature(feature, layer) {
    layer.on('mouseover', function () {
        this.setStyle({
    		weight: 5,
    		color: '#666',
    		dashArray: '',
    		fillOpacity: 0.1,
        fillColor: '#0000ff'    
            
        });
    });
    
    layer.on('mouseout', function () {
        this.setStyle({
    		weight: feature.properties.style.weight,
    		color: feature.properties.style.color,
    		fillOpacity: feature.properties.style.fillOpacity,
        fillColor:  feature.properties.style.fillColor           
        });
    });  
    

    layer.on({    
        click: zoomToFeature
    });   
        
    if (!L.Browser.ie && !L.Browser.opera && !L.Browser.edge) {
    	layer.bringToFront();
    }
            
    // does this feature have a property named popupContent?
    if (feature.properties && feature.properties.popupContent) {
        layer.bindPopup(feature.properties.popupContent);
    }
}


/*
function onEachFeature(feature, layer) {
	var popupContent = '<p>I started out as a GeoJSON ' +
			feature.geometry.type + ', but now I\'m a Leaflet vector!</p>';

	if (feature.properties && feature.properties.popupContent) {
		popupContent += feature.properties.popupContent;
	}

	layer.bindPopup(popupContent);
}
*/






//Adds a delay on removing the map of 10 ms. Likely needed to make sure other bits and pieces have finished loading. 
function removeWithTimeout(layer) {
  setTimeout(function() {
    map.removeLayer(layer);
  }, 10);
}




//Creates a function that serves as a replica of Python's .format
String.prototype.format = function () {
   var i = 0, args = arguments;
   return this.replace(/{}/g, function () {
      return typeof args[i] != 'undefined' ? args[i++] : '';
  });
};










//CUSTOM MARKERS AND ICONS ##################################################




//This custom marker adds a custom class to the existing marker classes
L.CustomMarker = L.Marker.extend({
    // Overwrite onAdd function
    onAdd: function(map) {

        // Run original onAdd function
        L.Marker.prototype.onAdd.call(this, map);

        // Check if there's a class set in options
        if (this.options.className) {

            // Apply className to icon and shadow
            L.DomUtil.addClass(this._icon, this.options.className);
            L.DomUtil.addClass(this._shadow, this.options.className);
        }

        // return instance
        return this;
    },

    // Function for checking class
    hasClass: function(name) {

        // Check if a class is set in options and compare to given one
        return this.options.className && this.options.className === name;
    }
});



//CUSTOM ICONS###############################################################



//Leaflet icon 
var greenIcon = L.icon({
    iconUrl: 'https://leafletjs.com/examples/custom-icons/leaf-green.png',
    shadowUrl: 'leaf-shadow.png',

    iconSize: [38, 95], // size of the icon
    shadowSize: [50, 64], // size of the shadow
    iconAnchor: [22, 94], // point of the icon which will correspond to marker's location
    shadowAnchor: [4, 62], // the same for the shadow
    popupAnchor: [-3, -76] // point from which the popup should open relative to the iconAnchor
});

var icon = new L.Icon.Default();
icon.options.shadowSize = [0, 0]; // Used in conjunction with line above and {icon : icon}, removes shadow from map. 
// Firefox icon
var firefoxIcon = L.icon({
    iconUrl: 'http://joshuafrazier.info/images/firefox.svg',
    iconSize: [38, 95], // size of the icon
    popupAnchor: [0, -15]
});


//###########################################################################

        
        



//GeoJSON Options ###########################################################

        



//Make layers ##############################################################





//Feature Groups ############################################################



  

//Make markers #################################################################






//Heat Maps ###################################################################





//Add MultiPolygons ############################################################






//Add tiles #################################################################







//Make map ##################################################################






//Layer control #############################################################








//If a feature group box is clicked on, it will force the markers to appear, even if the banner checkbox for the marker is not checked. 	
//Temporary solution is to turn all boxes on when a layer is selected. 
//checkFix ##################################################################








//Other Options ##################################################################









//Text boxes#################################################################







//Icon Legend ###############################################################









//FINAL JS ####################################################################


//Some JS to alter the look and hover text of the search by name icon 
//document.querySelector("#map > div.leaflet-control-container > div.leaflet-top.leaflet-left > div:nth-child(4) > a.search-button").style.backgroundColor = "#ADD8E6";
//document.querySelector("#map > div.leaflet-control-container > div.leaflet-top.leaflet-left > div:nth-child(4) > a.search-button").title = "Search By Name";



    </script>



</body>

</html>
"""


tiles ="""
//Mapbox
var mbAttr = 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>';
var mbUrl = 'https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw';
var streets = L.tileLayer(mbUrl, {id: 'mapbox/streets-v11', tileSize: 512, zoomOffset: -1, attribution: mbAttr});

//Open Street Map
var osm = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
	maxZoom: 19,
	attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
});


//Black and white (Stamen Tone Lite)
var Stamen_TonerLite = L.tileLayer('https://stamen-tiles-{s}.a.ssl.fastly.net/toner-lite/{z}/{x}/{y}{r}.{ext}', {
	attribution: 'Map tiles by <a href="http://stamen.com">Stamen Design</a>, <a href="http://creativecommons.org/licenses/by/3.0">CC BY 3.0</a> &mdash; Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
	subdomains: 'abcd',
	minZoom: 0,
	maxZoom: 20,
	ext: 'png'
});



//Google
var Google = L.tileLayer('http://www.google.cn/maps/vt?lyrs=s@189&gl=cn&x={x}&y={y}&z={z}', {
            attribution: 'google'
});









"""



