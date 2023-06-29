//const copy = "&copy; <a href='https://www.openstreetmap.org/copyright'>OpenStreetMap</a> contributors";
//const url = "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png";
//const layer = L.tileLayer(url, { attribution: copy });
//const map = L.map("map", { layers: [layer] });
//map.fitWorld();

let mapOptions = {
    center:[47.49493650511712, 36.175781451165676],
    zoom:10
}

let map = new L.map('map' , mapOptions);

let layer = new L.TileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png');
map.addLayer(layer);


let marker = null;
map.on('click', (event)=> {

    if(marker !== null){
        map.removeLayer(marker);
    }

    marker = L.marker([event.latlng.lat , event.latlng.lng]).addTo(map);

    document.getElementById('id_latitude').value = event.latlng.lat;
    document.getElementById('id_longitude').value = event.latlng.lng;

})


let popupOption = {
    "closeButton":false
}

locations.forEach(element => {
    new L.Marker([element.latitude,element.longitude]).addTo(map)
    .on("mouseover",event =>{
        event.target.bindPopup('<div class="card"><img src="'+element.src+'" width="80" height="80" alt="'+element.title+'">   <h3>'+element.title+'</h3></div>',popupOption).openPopup();
    })
    .on("mouseout", event => {
        event.target.closePopup();
    })
    .on("click" , () => {
        window.open(element.url);
    })
});
