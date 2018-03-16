// Creating map object
var myMap = L.map("map", {
  center: [37.8, -96],
  zoom: 4
});

// Adding tile layer
L.tileLayer("https://api.mapbox.com/styles/v1/mapbox/light-v9/tiles/256/{z}/{x}/{y}?access_token=pk.eyJ1IjoibWFydWJpbyIsImEiOiJjamU2aHdqaTgwMGpxMnFxd29sc2E3dmtyIn0.ONxJY7JvO7pewT7WKk5_Qg").addTo(myMap);

// Color scale for choropleth map. Copied from leaflet example.
function getColor(d) {
  return d > 1000 ? '#800026' :
         d > 500  ? '#BD0026' :
         d > 200  ? '#E31A1C' :
         d > 100  ? '#FC4E2A' :
         d > 50   ? '#FD8D3C' :
         d > 20   ? '#FEB24C' :
         d > 10   ? '#FED976' :
                    '#FFEDA0';
}

