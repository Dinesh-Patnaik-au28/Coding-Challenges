let googleMap_URL = 'http://www.google.com/maps/search/?api=1&query=';
const locationBtn = document.getElementById('getLocation');
const viewMapsBtn = document.getElementById('googleMaps');

locationBtn.addEventListener('click', locationHandler);
viewMapsBtn.addEventListener('click', viewMapsHandler);

function locationHandler() {
    if(navigator.geolocation){
        navigator.geolocation.getCurrentPosition(success, error);
    } else {
        alert('Geolocation is not supported by this browser');
    }
}

function success(pos) {
    console.log(pos);
    const lat = pos.coords.latitude;
    const log = pos.coords.longitude;
    googleMap_URL += `${lat},${log}`;
    const result = document.getElementById('result');
    result.innerHTML = `<p>Latitude is <span style = "font-weight: bold;">${lat}&deg;</span>, 
    Longitude is <span style = "font-weight: bold;">${log}&deg;</span></p>`;
}

function error(err) {
    console.log(err);
}

function viewMapsHandler() {
    window.open(googleMap_URL);
}