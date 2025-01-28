document.addEventListener('DOMContentLoaded', function() {
    const addEntryBtn = document.getElementById('add-entry-btn');
    const saveEntriesBtn = document.getElementById('save-entries-btn');
    const financialDetailsBody = document.getElementById('financial-details-body');
    const newEntryRow = document.getElementById('new-entry-row');

    function createNewRow() {
        const newRow = document.createElement('tr');
        newRow.innerHTML = `
            <td contenteditable="true"></td>
            <td contenteditable="true"></td>
            <td contenteditable="true"></td>
            <td contenteditable="true"></td>
            <td></td>
        `;
        financialDetailsBody.insertBefore(newRow, newEntryRow);
    }

    function validateRow(row) {
        const cells = row.querySelectorAll('td');
        const holdingTitle = cells[0].innerText.trim();
        const holdingPounds = cells[1].innerText.trim();
        const holdingShillings = cells[2].innerText.trim();
        const holdingPence = cells[3].innerText.trim();

        if (!holdingTitle || !holdingPounds || !holdingShillings || !holdingPence) {
            alert('All fields are required.');
            return false;
        }

        if (isNaN(holdingPounds) || isNaN(holdingShillings) || isNaN(holdingPence)) {
            alert('Pounds, Shillings, and Pence must be numeric values.');
            return false;
        }

        return true;
    }

    function showEditForm(detailId) {
        document.getElementById('edit-form-' + detailId).style.display = 'table-row';
    }
    
    function populateHiddenFields() {
        const lastRow = financialDetailsBody.querySelector('tr:last-child');
        if (validateRow(lastRow)) {
            document.getElementById('holding_title').value = lastRow.cells[0].innerText.trim();
            document.getElementById('holding_pounds').value = lastRow.cells[1].innerText.trim();
            document.getElementById('holding_shillings').value = lastRow.cells[2].innerText.trim();
            document.getElementById('holding_pence').value = lastRow.cells[3].innerText.trim();
        } else {
            alert('Please fill in all fields correctly before saving.');
        }
    }

    if (addEntryBtn) {
        addEntryBtn.addEventListener('click', function() {
            const rows = financialDetailsBody.querySelectorAll('tr');
            const lastRow = rows[rows.length - 1]; // The last row
            if (validateRow(lastRow)) {
                createNewRow();
            } else {
                alert('Please fill in all fields correctly before adding a new entry.');
            }
        });
    }

    if (saveEntriesBtn) {
        saveEntriesBtn.addEventListener('click', function(event) {
            populateHiddenFields();
        });
    }
});

