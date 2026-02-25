function initializeCompressorForm() {
    const form = document.getElementById('compressForm');
    if (!form) return;

    form.addEventListener('submit', function (event) {
        event.preventDefault();
        const formData = new FormData(this);
        const customBitrate = document.getElementById('customBitrate').value;

        if (customBitrate) {
            formData.set('bitrate', customBitrate + 'k');
        }

        showSpinner();
        clearStatus();

        fetch('/compress', {
            method: 'POST',
            body: formData
        })
            .then(response => {
                if (!response.ok) throw new Error('Network response was not ok');
                return response.json();
            })
            .then(result => {
                hideSpinner();
                if (result.errors) {
                    result.errors.forEach(error => {
                        showStatus(error, 'danger');
                    });
                }
                if (result.successes) {
                    result.successes.forEach(success => {
                        showStatus(success, 'success');
                    });
                    updateFileList();
                    form.reset();
                }
            })
            .catch(error => {
                console.error('Error:', error);
                hideSpinner();
                showStatus('An error occurred during compression: ' + error.message, 'danger');
            });
    });
}

function initializeConverterForm() {
    const form = document.getElementById('convertForm');
    if (!form) return;

    form.addEventListener('submit', function (event) {
        event.preventDefault();
        const formData = new FormData(this);
        showSpinner();
        clearStatus();

        fetch('/convert', {
            method: 'POST',
            body: formData
        })
            .then(response => {
                if (!response.ok) throw new Error('Network response was not ok');
                return response.json();
            })
            .then(result => {
                hideSpinner();
                if (result.errors && result.errors.length > 0) {
                    result.errors.forEach(error => {
                        showStatus(error, 'danger');
                    });
                }
                if (result.successes && result.successes.length > 0) {
                    result.successes.forEach(success => {
                        showStatus(success, 'success');
                    });
                    updateFileList();
                    form.reset();
                }
                if (!result.errors && !result.successes) {
                    throw new Error('Invalid response format');
                }
            })
            .catch(error => {
                console.error('Error:', error);
                hideSpinner();
                showStatus('An error occurred during conversion: ' + error.message, 'danger');
            });
    });
}

function initializeRenamerForm() {
    const form = document.getElementById('renameForm');
    if (!form) return;

    form.addEventListener('submit', function (event) {
        event.preventDefault();
        const formData = new FormData(this);
        showSpinner();
        clearStatus();

        fetch('/rename', {
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
                    showStatus('Files renamed successfully!');
                    updateFileList();
                    form.reset();
                } else if (result.error) {
                    showStatus(result.error, 'danger');
                } else {
                    throw new Error('Invalid response format');
                }
            })
            .catch(error => {
                console.error('Error:', error);
                hideSpinner();
                showStatus('An error occurred during renaming: ' + error.message, 'danger');
            });
    });
}

function initializeDownloaderForm() {
    const form = document.getElementById('downloadForm');
    if (!form) return;

    form.addEventListener('submit', function (event) {
        event.preventDefault();
        const url = document.getElementById('url').value;
        const formData = new FormData();
        formData.append('url', url);
        showSpinner();
        clearStatus();

        fetch('/download', {
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
                    showStatus('Video downloaded successfully!', 'success');
                    updateFileList();
                    form.reset();
                } else if (result.error) {
                    showStatus(result.error, 'danger');
                }
            })
            .catch(error => {
                console.error('Error:', error);
                hideSpinner();
                showStatus('An error occurred during download: ' + error.message, 'danger');
            });
    });
}

function isValidUrl(url) {
    try {
        new URL(url);
        return true;
    } catch {
        return false;
    }
}