document.addEventListener('DOMContentLoaded', function() {
    const religiousOrderSelect = document.getElementById('id_religious_order');
    const otherReligiousOrderField = document.getElementById('id_other_religious_order');

    function toggleOtherField() {
        if (religiousOrderSelect.value === 'other') {
            otherReligiousOrderField.parentElement.style.display = 'block';
        } else {
            otherReligiousOrderField.parentElement.style.display = 'none';
        }
    }

    religiousOrderSelect.addEventListener('change', toggleOtherField);
    toggleOtherField();  // Initial call to set the correct state
});