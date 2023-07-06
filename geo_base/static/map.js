    let combatIcon= {
        iconUrl: "/static/images/marker-icon-blue.png",
        iconSize: [25,41]
}


    let myIcon2 = L.icon(combatIcon);

    let icon2Options = {
        title: "combat_unit.type",
        draggable: true,
        icon: myIcon2,
}


initial_position = [47.49493650511712, 36.175781451165676]


         if ( window.location.pathname=="/geo_base/position/"){
             if (locationsCU.latitudeC) {
                            initial_position = [locationsCU.latitudeC, locationsCU.longitudeC]
                    }
         }

        let mapOptions= {
        center: initial_position,
        zoom: 10
         }


let map = new L.map('map', mapOptions);
    let layer= new L.TileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png');
    map.addLayer(layer);


 if ( window.location.pathname=="/geo_base/position/" ) {
     if (locationsCU.latitudeC) {
                   new L.Marker([locationsCU.latitudeC, locationsCU.longitudeC], icon2Options).addTo(map)
            }
 }


    if ( window.location.pathname=="/geo_base/position/" ) {


        let targetIcon= {
        iconUrl: "/static/images/marker-icon-red.png",
        iconSize: [25,41]
        }

        let myIcon = L.icon(targetIcon);

        let iconOptions = {
        title: "target.type",
        draggable: true,
        icon: myIcon,
        }


if (typeof locations !== 'undefined'){
            locations.forEach(element => {

                    new L.Marker([element.latitude,element.longitude], iconOptions).addTo(map)
                    .on("mouseover", event => {
                        event.target.bindPopup('<div class="card"> <img src="'+element.target_img_path+'" width="80" height="55" alt="'+element.type+'"> <h3>'+element.distance+'</h3> </div>',popupOption).openPopup();
                    })
                    .on("mouseout", event => {
                        event.target.closePopup();
                    })

            })

            new L.Marker([locationsCU.latitudeC, locationsCU.longitudeC], icon2Options).addTo(map)

}
    }



    let popupOption= {
    "closeButton":false
    }


//get marker coordinates

    let marker = null;
    map.on('click', (event)=> {

            if(marker !== null) {
                map.removeLayer(marker);
            }

            marker = L.marker([event.latlng.lat, event.latlng.lng], icon2Options).addTo(map);

            document.getElementById('id_latitude').value = event.latlng.lat;
            document.getElementById('id_longitude').value = event.latlng.lng;
    })
