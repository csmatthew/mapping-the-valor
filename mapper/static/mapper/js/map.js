console.log('map.js loaded');

document.addEventListener('DOMContentLoaded', function () {
    console.log('DOM fully loaded and parsed');
    var mapContainer = document.getElementById('map');

    if (mapContainer && !mapContainer._leaflet_map) {
        var map = L.map('map', {
            center: [53.5, -2.25], // Centered on Manchester
            zoom: 10,
            minZoom: 6, // Prevent zooming out further than zoom level 6
            maxBounds: [
                [49.5, -10.5], // Southwest corner
                [59, 2]       // Northeast corner
            ],
            maxBoundsViscosity: 1.0 // Ensures the map is completely restricted to the bounds
        });
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
                        let name = record.name;
                        if (record.house_type) {
                            name += ` ${record.house_type}`;
                        } else if (record.record_type !== 'Monastery') {
                            name += ` ${record.record_type}`;
                        }
                        let popupContent = `<b>${name}</b><br>
                                            Record Type: ${record.record_type}<br>
                                            Deanery: ${record.deanery}<br>`;
                        if (record.religious_order) {
                            popupContent += `Religious Order: ${record.religious_order}<br>`;
                        }
                        popupContent += `<button onclick="window.location.href='/valor-records/${record.slug}/'">View Details</button>`;
                        let marker = L.marker([record.latitude, record.longitude])
                            .addTo(map)
                            .bindPopup(popupContent);

                        // Add click event to zoom in when marker is selected
                        var isPopupOpen = false;
                        marker.on('click', function() {
                            isPopupOpen = true;
                            marker.openPopup();
                            map.flyTo([record.latitude, record.longitude], 15, {
                                animate: true,
                                duration: 2 // Duration in seconds
                            }); // Zoom in to the marker location with a smooth transition
                        });

                        // Handle marker hover events
                        marker.on('mouseover', function() {
                            if (!isPopupOpen) {
                                marker.openPopup();
                            }
                        });

                        marker.on('mouseout', function() {
                            if (!isPopupOpen) {
                                marker.closePopup();
                            }
                        });

                        map.on('click', function() {
                            isPopupOpen = false;
                            marker.closePopup();
                        });
                    }
                });
            })
            .catch(error => console.error('Error fetching valor records:', error));
    }
});