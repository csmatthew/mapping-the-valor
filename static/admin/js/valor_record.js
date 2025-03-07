document.addEventListener('DOMContentLoaded', function () {
    const recordTypeField = document.querySelector('#id_record_type');
    const houseTypeField = document.querySelector('.field-house_type');

    function toggleHouseTypeField() {
        if (recordTypeField.value === 'Monastery') {
            houseTypeField.style.display = '';
        } else {
            houseTypeField.style.display = 'none';
        }
    }

    // Initial check
    toggleHouseTypeField();

    // Add event listener to record type field
    recordTypeField.addEventListener('change', toggleHouseTypeField);
});
