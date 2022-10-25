//Initialize map
function initMap() {
  //the location of asuncion
  const asuncion = { lat: -25.3396, lng: -57.612 };
  //the map centered at asuncion
  const map = new google.maps.Map(document.getElementById("map"), {
    zoom: 6,
    center: asuncion,
  });
  //create marker
  let marker = new google.maps.Marker({
    position: asuncion,
    map: map,
  });

  //map receives click
  map.addListener("click", (e) => {
    //get latitude and longitude values
    let latLng = e.latLng.toJSON();
    //get latitude and longitude input
    //select inputs
    const latInput = document.getElementById("latitude");
    const lngInput = document.getElementById("longitude");
    console.log(latInput);
    latInput.value = latLng.lat;
    lngInput.value = latLng.lng;
    //delete previous marker
    marker.setMap(null);
    //create new marker based on click
    marker = new google.maps.Marker({
      position: e.latLng,
      map: map,
    });
  });
}

window.initMap = initMap;
