// Function to toggle edit mode for a row
function toggleEditMode(rowId) {
    const row = document.getElementById(`row-${rowId}`);
    const cells = row.querySelectorAll(".editable");

    // Toggle contenteditable on/off
    cells.forEach((cell) => {
        const isEditable = cell.getAttribute("contenteditable") === "true";
        cell.setAttribute("contenteditable", !isEditable);
    });

    // Update the button label
    const editButton = row.querySelector(".edit-button");
    editButton.textContent = cells[0].getAttribute("contenteditable") === "true" ? "Save" : "Edit";

    // If saving, gather data
    if (editButton.textContent === "Edit") {
        saveRow(rowId);
    }
}

// Function to save row data
function saveRow(rowId) {
    const row = document.getElementById(`row-${rowId}`);
    const data = {
        id: rowId,
        holding_title: row.querySelector(".holding-title").textContent.trim(),
        holding_pounds: row.querySelector(".holding-pounds").textContent.trim(),
        holding_shillings: row.querySelector(".holding-shillings").textContent.trim(),
        holding_pence: row.querySelector(".holding-pence").textContent.trim(),
    };

    // Send data to the server using fetch
    fetch(`/update-financial-detail/`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": "{{ csrf_token }}", // Include CSRF token
            },
            body: JSON.stringify(data),
        })
        .then((response) => {
            if (response.ok) {
                return response.json();
            } else {
                throw new Error("Failed to save changes");
            }
        })
        .then((result) => {
            console.log("Row saved successfully:", result);
        })
        .catch((error) => {
            console.error("Error:", error);
            alert("An error occurred while saving the data.");
        });
}

// For handling CRUD operations via AJAX
document.addEventListener('DOMContentLoaded', function () {

    // Handle form submission for new entries
    const addForm = document.querySelector("#financial-details-form");
    if (addForm) {
        addForm.addEventListener('submit', function (event) {
            event.preventDefault(); // Prevent default form submission

            const formData = new FormData(addForm); // Get the form data
            fetch(window.location.href, { // Send it to the current page
                    method: 'POST',
                    body: formData,
                })
                .then(response => response.json())
                .then(data => {
                    if (data.success) {
                        alert(data.message); // Show success message
                        location.reload(); // Reload the page to reflect changes (or you can update the table dynamically)
                    } else {
                        alert(data.message); // Show error message
                    }
                })
                .catch(error => {
                    alert("An error occurred: " + error);
                });
        });
    }

    // Handle form submission for updating existing entries
    const editForms = document.querySelectorAll('.financial-edit-form');
    editForms.forEach(form => {
        form.addEventListener('submit', function (event) {
            event.preventDefault(); // Prevent default form submission

            const formData = new FormData(form); // Get the form data
            fetch(window.location.href, { // Send it to the current page
                    method: 'POST',
                    body: formData,
                })
                .then(response => response.json())
                .then(data => {
                    if (data.success) {
                        alert(data.message); // Show success message
                        location.reload(); // Reload the page to reflect changes
                    } else {
                        alert(data.message); // Show error message
                    }
                })
                .catch(error => {
                    alert("An error occurred: " + error);
                });
        });
    });

    // Handle delete button clicks
    const deleteButtons = document.querySelectorAll('.delete-detail-button');
    deleteButtons.forEach(button => {
        button.addEventListener('click', function (event) {
            event.preventDefault(); // Prevent default button action

            const detailId = this.getAttribute('data-detail-id'); // Get the detail ID from the button's data attribute
            const formData = new FormData();
            formData.append('detail_id', detailId);
            formData.append('delete_detail', true);

            fetch(window.location.href, { // Send the data to the current page
                    method: 'POST',
                    body: formData,
                })
                .then(response => response.json())
                .then(data => {
                    if (data.success) {
                        alert(data.message); // Show success message
                        location.reload(); // Reload the page to reflect changes
                    } else {
                        alert(data.message); // Show error message
                    }
                })
                .catch(error => {
                    alert("An error occurred: " + error);
                });
        });
    });
});

document.addEventListener('DOMContentLoaded', function() {
    // Handle the 'Add Entry' button click event
    document.getElementById('add-entry')?.addEventListener('click', function(event) {
        event.preventDefault();

        let row = document.getElementById('new-entry-row');
        let holdingTitle = row.cells[0].textContent.trim();
        let holdingPounds = row.cells[1].textContent.trim();
        let holdingShillings = row.cells[2].textContent.trim();
        let holdingPence = row.cells[3].textContent.trim();

        let formData = new FormData();
        formData.append('holding_title', holdingTitle);
        formData.append('holding_pounds', holdingPounds);
        formData.append('holding_shillings', holdingShillings);
        formData.append('holding_pence', holdingPence);
        
        // Get the CSRF token
        formData.append('csrfmiddlewaretoken', document.querySelector('[name=csrfmiddlewaretoken]').value);

        // Send the data via AJAX
        fetch(window.location.href, {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                // If the entry was added successfully, append it to the table
                let newRow = document.createElement('tr');
                newRow.innerHTML = `
                    <td>${data.holding_title}</td>
                    <td>${data.holding_pounds}</td>
                    <td>${data.holding_shillings}</td>
                    <td>${data.holding_pence}</td>
                    <td>${data.total_lsd}</td>
                    <td>
                        <button type="button" class="btn btn-secondary" onclick="showEditForm('${data.id}')">Edit</button>
                        <form method="post" style="display: inline;">
                            {% csrf_token %}
                            <input type="hidden" name="detail_id" value="${data.id}">
                            <button type="submit" name="delete_detail" class="btn btn-danger">Delete</button>
                        </form>
                    </td>
                `;
                document.getElementById('financial-details-body').appendChild(newRow);
                row.cells[0].textContent = '';
                row.cells[1].textContent = '';
                row.cells[2].textContent = '';
                row.cells[3].textContent = '';
            } else {
                alert('Failed to add entry');
            }
        });
    });

    // Handle the edit form submission
    document.querySelectorAll('.edit-form').forEach(function(editForm) {
        editForm.addEventListener('submit', function(event) {
            event.preventDefault();
            let formData = new FormData(editForm);

            fetch(window.location.href, {
                method: 'POST',
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    let row = document.getElementById(`detail-${data.id}`);
                    row.querySelector('td:nth-child(1)').textContent = data.holding_title;
                    row.querySelector('td:nth-child(2)').textContent = data.holding_pounds;
                    row.querySelector('td:nth-child(3)').textContent = data.holding_shillings;
                    row.querySelector('td:nth-child(4)').textContent = data.holding_pence;
                    row.querySelector('td:nth-child(5)').textContent = data.total_lsd;
                    document.getElementById(`edit-form-${data.id}`).style.display = 'none';
                } else {
                    alert('Failed to update entry');
                }
            });
        });
    });

    // Handle delete button click (AJAX delete)
    document.querySelectorAll('.delete-form').forEach(function(deleteForm) {
        deleteForm.addEventListener('submit', function(event) {
            event.preventDefault();
            let formData = new FormData(deleteForm);

            fetch(window.location.href, {
                method: 'POST',
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    let row = document.getElementById(`detail-${data.id}`);
                    row.remove();
                } else {
                    alert('Failed to delete entry');
                }
            });
        });
    });
});

// Handle form submission for create/update/delete operations
$('form').on('submit', function(event) {
    event.preventDefault();  // Prevent default form submission

    let form = $(this);
    let url = form.attr('action');
    let formData = form.serialize();  // Serialize form data

    $.ajax({
        type: form.attr('method'),
        url: url,
        data: formData,
        success: function(response) {
            if (response.success) {
                // Handle success (e.g., update UI with new data)
                alert(response.message);  // Show success message
                location.reload();  // Reload the page or update the UI as needed
            } else {
                // Handle failure (e.g., show error message)
                alert(response.message);  // Show error message
            }
        },
        error: function(xhr, status, error) {
            // Handle AJAX error
            alert('An error occurred. Please try again later.');
        }
    });
});
