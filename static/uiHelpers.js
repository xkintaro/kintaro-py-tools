function showSpinner() {
    const spinner = document.getElementById('loadingSpinner');
    if (spinner) spinner.style.display = 'block';
}

function hideSpinner() {
    const spinner = document.getElementById('loadingSpinner');
    if (spinner) spinner.style.display = 'none';
}

function showStatus(message, type = 'success') {
    const statusDiv = document.getElementById('status');
    if (!statusDiv) return;

    const alertDiv = document.createElement('div');
    alertDiv.className = `alert alert-${type} mb-2`;
    alertDiv.textContent = message;
    statusDiv.appendChild(alertDiv);

    setTimeout(() => {
        if (alertDiv.parentNode === statusDiv) {
            alertDiv.remove();
            if (!statusDiv.hasChildNodes()) {
                clearStatus();
            }
        }
    }, 5000);
}

function clearStatus() {
    const statusDiv = document.getElementById('status');
    if (statusDiv) statusDiv.innerHTML = '';
}