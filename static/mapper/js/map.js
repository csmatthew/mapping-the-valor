document.addEventListener('DOMContentLoaded', function () {
    var mapContainer = document.getElementById('map');

    if (mapContainer && !mapContainer._leaflet_map) {
        var map = L.map('map').setView([54.5, -3], 6); // Centered on Britain
        mapContainer._leaflet_map = map;

        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            attribution: '&copy; OpenStreetMap contributors'
        }).addTo(map);

        // Fetch Valor Records and add them to the map
        fetch('/map/valor-records/')
            .then(response => response.json())
            .then(data => {
                data.forEach(record => {
                    if (record.latitude && record.longitude) {
                        let name = record.name;
                        if (record.house_type) {
                            name += ` ${record.house_type}`;
                        } else if (record.record_type !== 'Monastery') {
                            name += ` ${record.record_type}`;
                        }
                        let popupContent = `<b>${name}</b><br>
                                            Record Type: ${record.record_type}<br>
                                            Deanery: ${record.deanery}<br>
                                            <button onclick="window.location.href='/valor-records/${record.slug}/'">View Details</button>`;
                        let marker = L.marker([record.latitude, record.longitude])
                            .addTo(map)
                            .bindPopup(popupContent);

                        // Add click event to zoom in when marker is selected
                        marker.on('click', function() {
                            map.flyTo([record.latitude, record.longitude], 15, {
                                animate: true,
                                duration: 2 // Duration in seconds
                            }); // Zoom in to the marker location with a smooth transition
                        });
                    }
                });
            })
            .catch(error => console.error('Error fetching valor records:', error));
    }
});