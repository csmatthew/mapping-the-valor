console.log('map.js loaded');

document.addEventListener('DOMContentLoaded', function () {
    console.log('DOM fully loaded and parsed');
    var mapContainer = document.getElementById('map');

    if (mapContainer && !mapContainer._leaflet_map) {
        var map = L.map('map').setView([54.5, -3], 6); // Centered on Britain
        mapContainer._leaflet_map = map;
        console.log('Map initialized:', map);

        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            attribution: '&copy; OpenStreetMap contributors'
        }).addTo(map);

        // Fetch Valor Records and add them to the map
        fetch('/map/valor-records/')
            .then(response => response.json())
            .then(data => {
                console.log('Valor Records:', data); // Log the data to verify the response
                data.forEach(record => {
                    if (record.latitude && record.longitude) {
                        L.marker([record.latitude, record.longitude])
                            .addTo(map)
                            .bindPopup(`<b>${record.name}</b><br>${record.record_type}`);
                    }
                });
            })
            .catch(error => console.error('Error fetching valor records:', error));
    }
});