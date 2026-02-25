function confirmClearFolder(folder) {
    if (confirm('Are you sure you want to clear all files in this folder?')) {
        clearFolder(folder);
    }
}

function clearFolder(folder) {
    if (!folder) {
        showStatus('Invalid folder specified', 'danger');
        return;
    }

    const formData = new FormData();
    formData.append('folder', folder);
    showSpinner();
    clearStatus();

    fetch('/clear', {
        method: 'POST',
        body: formData
    })
        .then(response => {
            if (!response.ok) throw new Error('Network response was not ok');
            return response.json();
        })
        .then(result => {
            hideSpinner();
            if (result.success) {
                showStatus('Folder cleared successfully!');
                updateFileList();
            } else {
                showStatus(result.error || 'An error occurred during clearing.', 'danger');
            }
        })
        .catch(error => {
            console.error('Error:', error);
            hideSpinner();
            showStatus('An error occurred during clearing: ' + error.message, 'danger');
        });
}

function openFolder(folder) {
    if (!folder) {
        showStatus('Invalid folder specified', 'danger');
        return;
    }

    const formData = new FormData();
    formData.append('folder', folder);

    fetch('/open_folder', {
        method: 'POST',
        body: formData
    })
        .then(response => {
            if (!response.ok) throw new Error('Network response was not ok');
            return response.json();
        })
        .then(result => {
            if (!result.success) {
                showStatus(result.error || 'An error occurred while opening the folder.', 'danger');
            }
        })
        .catch(error => {
            console.error('Error:', error);
            showStatus('An error occurred while opening the folder: ' + error.message, 'danger');
        });
}