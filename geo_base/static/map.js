    initial_position = [47.49493650511712, 36.175781451165676]

    location_exist = locationsCU

    if (locationsCU.latitudeC) {
        initial_position = [locationsCU.latitudeC, locationsCU.longitudeC]
}

    let mapOptions= {
        center: initial_position,
        zoom: 10
}

    let map = new L.map('map', mapOptions);

    let layer= new L.TileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png');
    map.addLayer(layer);

    let targetIcon= {
        iconUrl: "../static/images/marker-icon-red.png",
        iconSize: [25,41]
}

    let combatIcon= {
        iconUrl: "../geo_base/static/images/marker-icon-blue.png",
        iconSize: [25,41]
}

    let myIcon = L.icon(targetIcon);

    let myIcon2 = L.icon(combatIcon);

    let iconOptions = {
        title: "target.type",
        draggable: true,
        icon: myIcon,
}

    let icon2Options = {
        title: "combat_unit.type",
        draggable: true,
        icon: myIcon2,
}

    let marker = null;
    map.on('click', (event)=> {

        if(marker !== null) {
            map.removeLayer(marker);
        }

        marker = L.marker([event.latlng.lat, event.latlng.lng], icon2Options).addTo(map);

        document.getElementById('id_latitude').value = event.latlng.lat;
        document.getElementById('id_longitude').value = event.latlng.lng;
})

    let popupOption= {
    "closeButton":false
}

    if (locationsCU.latitudeC) {
            new L.Marker([locationsCU.latitudeC, locationsCU.longitudeC], icon2Options).addTo(map)
}

    locations.forEach(element => {

    new L.Marker([element.latitude,element.longitude], iconOptions).addTo(map)
    .on("mouseover", event => {
        event.target.bindPopup('<div class="card"> <img src="'+element.target_img_path+'" width="80" height="55" alt="'+element.type+'"> <h3>'+element.distance+'</h3> </div>',popupOption).openPopup();
    })
    .on("mouseout", event => {
        event.target.closePopup();
    })

})

