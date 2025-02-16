document.addEventListener('DOMContentLoaded', function () {
    var mapContainer = document.getElementById('map');
    if (mapContainer && !mapContainer._leaflet_map) {
        var map = L.map('map').setView([54.5, -3], 6); // Centered on Britain
        mapContainer._leaflet_map = map;

        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            attribution: '&copy; OpenStreetMap contributors'
        }).addTo(map);

        // Handle overlay click event
        var mapOverlay = document.getElementById('map-overlay');
        var mapOverlayText = document.getElementById('map-overlay-text');

        // Detect if the device is a touch device
        var isTouchDevice = 'ontouchstart' in window || navigator.maxTouchPoints > 0;

        if (isTouchDevice) {
            // Add touch-specific event handling here
        } else {
            mapOverlayText.textContent = 'Click to activate map';
        }

        mapOverlay.addEventListener('click', function () {
            mapOverlay.style.display = 'none';
        });
    }
});