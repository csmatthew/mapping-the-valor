console.log('map.js loaded');

document.addEventListener('DOMContentLoaded', function () {
    console.log('DOM fully loaded and parsed');
    var mapContainer = document.getElementById('map');
    var pinPlacementEnabled = false;

    if (mapContainer && !mapContainer._leaflet_map) {
        var map = L.map('map').setView([54.5, -3], 6); // Centered on Britain
        mapContainer._leaflet_map = map;
        console.log('Map initialized:', map);

        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            attribution: '&copy; OpenStreetMap contributors'
        }).addTo(map);

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
    }
});