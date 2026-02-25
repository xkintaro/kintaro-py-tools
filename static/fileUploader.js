function initializeDropzone(folder) {
    if (!folder) {
        console.error('Folder parameter is required for dropzone initialization');
        return;
    }

    const dropzone = document.getElementById('dropzone');
    const fileInput = document.getElementById('fileInput');

    if (!dropzone || !fileInput) {
        console.error('Required dropzone elements not found');
        return;
    }

    const newFileInput = fileInput.cloneNode(true);
    fileInput.parentNode.replaceChild(newFileInput, fileInput);
    const newDropzone = dropzone.cloneNode(true);
    dropzone.parentNode.replaceChild(newDropzone, dropzone);

    newFileInput.addEventListener('change', function (event) {
        if (event.target.files.length > 0) {
            uploadFiles(event.target.files, folder);
        }
    });

    newDropzone.addEventListener('dragover', function (event) {
        event.preventDefault();
        event.stopPropagation();
        this.classList.add('dragover');
    });

    newDropzone.addEventListener('dragleave', function (event) {
        event.preventDefault();
        event.stopPropagation();
        this.classList.remove('dragover');
    });

    newDropzone.addEventListener('drop', function (event) {
        event.preventDefault();
        event.stopPropagation();
        this.classList.remove('dragover');
        if (event.dataTransfer.files.length > 0) {
            uploadFiles(event.dataTransfer.files, folder);
        }
    });

    newDropzone.addEventListener('click', function () {
        newFileInput.click();
    });

    newFileInput.addEventListener('click', function () {
        this.value = '';
    });
}

function uploadFiles(files, folder) {
    if (!files || !folder) {
        showStatus('Invalid files or folder specified', 'danger');
        return;
    }

    const formData = new FormData();
    for (let i = 0; i < files.length; i++) {
        formData.append('files[]', files[i]);
    }
    formData.append('folder', folder);
    showSpinner();
    clearStatus();

    fetch('/upload', {
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
                showStatus('Files uploaded successfully!');
                updateFileList();
            } else {
                showStatus(result.error || 'An error occurred during upload.', 'danger');
            }
        })
        .catch(error => {
            console.error('Error:', error);
            hideSpinner();
            showStatus('An error occurred during upload: ' + error.message, 'danger');
        });
}