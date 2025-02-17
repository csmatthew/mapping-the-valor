document.addEventListener('DOMContentLoaded', function () {
    var mapContainer = document.getElementById('map');
    if (mapContainer && !mapContainer._leaflet_map) {
        var map = L.map('map').setView([54.5, -3], 6); // Centered on Britain
        mapContainer._leaflet_map = map;

        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            attribution: '&copy; OpenStreetMap contributors'
        }).addTo(map);

        // Handle overlay button click event
        var mapOverlayButton = document.getElementById('map-overlay-button');

        mapOverlayButton.addEventListener('click', function () {
            var mapOverlay = document.getElementById('map-overlay');
            mapOverlay.style.display = 'none';
        });
    }
});