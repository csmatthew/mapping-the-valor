console.log('map.js loaded');

document.addEventListener('DOMContentLoaded', function () {
    console.log('DOM fully loaded and parsed');
    var mapContainer = document.getElementById('map');
    var pinPlacementEnabled = false;
    var markers = []; // Array to store the markers

    if (mapContainer && !mapContainer._leaflet_map) {
        var map = L.map('map').setView([54.5, -3], 6); // Centered on Britain
        mapContainer._leaflet_map = map;
        console.log('Map initialized:', map);

        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            attribution: '&copy; OpenStreetMap contributors'
        }).addTo(map);

        // Fetch and plot monastery data
        fetch("/records/monasteries-json/")
            .then(response => {
                if (!response.ok) {
                    throw new Error(`HTTP error! Status: ${response.status}`);
                }
                return response.json();
            })
            .then(data => {
                console.log('Monastery data:', data); // Log the fetched data
                data.forEach(monastery => {
                    if (monastery.latitude && monastery.longitude) {
                        var marker = L.marker([monastery.latitude, monastery.longitude])
                            .bindPopup(
                                `<b>${monastery.name}</b><br>
                                House Type: ${monastery.house_type}<br>
                                Religious Order: ${monastery.religious_order}<br>
                                Abbot: ${monastery.abbot}<br>
                                Source: ${monastery.source}`
                            );
                        markers.push(marker); // Add marker to the array
                        // Do not add marker to the map initially
                        console.log('Marker prepared at:', monastery.latitude, monastery.longitude);

                        var isPopupOpen = false;

                        marker.on('click', function() {
                            isPopupOpen = true;
                            marker.openPopup();
                            map.flyTo([monastery.latitude, monastery.longitude], 15, {
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
                    } else {
                        console.log('Missing coordinates for:', monastery.name);
                    }
                });
            })
            .catch(error => {
                console.error('Error fetching monastery data:', error);
            });

        // Handle overlay button click event
        var mapOverlayButton = document.getElementById('map-overlay-button');

        mapOverlayButton.addEventListener('click', function () {
            var mapOverlay = document.getElementById('map-overlay');
            mapOverlay.style.display = 'none';
        });

        // Handle toggle pin placement button click event
        var togglePinPlacementButton = document.getElementById('toggle-pin-placement');

        togglePinPlacementButton.addEventListener('click', function () {
            pinPlacementEnabled = !pinPlacementEnabled;
            togglePinPlacementButton.textContent = pinPlacementEnabled ? 'Disable Pin Placement' : 'Enable Pin Placement';
        });

        // Handle map click event to place a pin
        map.on('click', function (e) {
            console.log('Map clicked:', e);
            if (pinPlacementEnabled && document.getElementById('pin-form-container')) {
                var latitude = e.latlng.lat;
                var longitude = e.latlng.lng;

                // Place a pin on the map
                var marker = L.marker([latitude, longitude]).addTo(map);
                console.log('Marker added at:', latitude, longitude);

                // Fill the form with the pin location
                document.getElementById('pin-latitude').value = latitude;
                document.getElementById('pin-longitude').value = longitude;

                // Show the form
                document.getElementById('pin-form-container').style.display = 'block';

                // Disable pin placement
                pinPlacementEnabled = false;
                togglePinPlacementButton.textContent = 'Enable Pin Placement';
                console.log('Pin placement disabled');
            }
        });

        // Handle monastery toggle button click event to toggle marker visibility
        var monasteryToggleButton = document.getElementById('monastery-toggle-button');
        var markersVisible = false;

        monasteryToggleButton.addEventListener('click', function () {
            markersVisible = !markersVisible;
            markers.forEach(marker => {
                if (markersVisible) {
                    marker.addTo(map);
                } else {
                    map.removeLayer(marker);
                }
            });
            monasteryToggleButton.textContent = markersVisible ? 'Hide Monasteries' : 'Show Monasteries';
        });
    }
});