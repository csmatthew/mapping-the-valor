console.log('map.js loaded');

document.addEventListener('DOMContentLoaded', function () {
    console.log('DOM fully loaded and parsed');
    var mapContainer = document.getElementById('map');

    if (mapContainer && !mapContainer._leaflet_map) {
        var map = L.map('map', {
            center: [53.5, -2.25], // Centered on Manchester
            zoom: 10, // Set initial zoom level to 10 for a more zoomed-in view
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
                        let marker = L.marker([record.latitude, record.longitude])
                            .addTo(map)
                            .bindPopup(popupContent);

                        // Add click event to show modal when marker is selected
                        marker.on('click', function() {
                            // Fetch the record details using the record slug
                            fetch(`/valor-records/${record.slug}/modal/`)
                                .then(response => response.text())
                                .then(html => {
                                    // Populate the modal content
                                    var modalContent = document.getElementById('modal-content');
                                    modalContent.innerHTML = html;
                                    // Show the modal
                                    var viewCardModal = new bootstrap.Modal(document.getElementById('viewCardModal'));
                                    viewCardModal.show();
                                })
                                .catch(error => console.error('Error fetching record details:', error));
                        });

                        // Handle marker hover events
                        marker.on('mouseover', function() {
                            marker.openPopup();
                        });

                        marker.on('mouseout', function() {
                            marker.closePopup();
                        });
                    }
                });
            })
            .catch(error => console.error('Error fetching valor records:', error));
    }
});