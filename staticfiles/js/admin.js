// JS for django admin

document.addEventListener('DOMContentLoaded', function() {
    const typeField = document.querySelector('#id_type');
    const monasteryInline = document.querySelector('.inline-related.monastery');

    console.log('Type field:', typeField);
    console.log('Monastery inline:', monasteryInline);

    function toggleMonasteryInline() {
        if (monasteryInline) {
            if (typeField.value === 'monastery') {
                monasteryInline.style.display = 'block';
                console.log('Monastery inline shown');
            } else {
                monasteryInline.style.display = 'none';
                console.log('Monastery inline hidden');
            }
        }
    }

    // Initial check
    toggleMonasteryInline();

    // Add event listener to type field
    if (typeField) {
        typeField.addEventListener('change', toggleMonasteryInline);
    }
});