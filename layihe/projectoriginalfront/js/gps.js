let map;

function initMap() {
  map = new google.maps.Map(document.getElementById("gps"), {
    center: { lat: 40.346108801959396, lng: 49.77653010129347 },
    zoom: 8,
  });
}