function updateFileList() {
    fetch(window.location.href)
        .then(response => {
            if (!response.ok) throw new Error('Network response was not ok');
            return response.text();
        })
        .then(html => {
            const parser = new DOMParser();
            const doc = parser.parseFromString(html, 'text/html');

            const startPreview = document.querySelector('#start-preview');
            const docStartPreview = doc.querySelector('#start-preview');
            if (startPreview && docStartPreview) {
                startPreview.innerHTML = docStartPreview.innerHTML;
            }

            const finishPreview = document.querySelector('#finish-preview');
            const docFinishPreview = doc.querySelector('#finish-preview');
            if (finishPreview && docFinishPreview) {
                finishPreview.innerHTML = docFinishPreview.innerHTML;
            }

            const downloadsPreview = document.querySelector('#downloads-preview');
            const docDownloadsPreview = doc.querySelector('#downloads-preview');
            if (downloadsPreview && docDownloadsPreview) {
                downloadsPreview.innerHTML = docDownloadsPreview.innerHTML;
            }

            const headingStart = document.querySelector('#headingStart button');
            const docHeadingStart = doc.querySelector('#headingStart button');
            if (headingStart && docHeadingStart) {
                headingStart.innerHTML = docHeadingStart.innerHTML;
            }

            const headingFinish = document.querySelector('#headingFinish button');
            const docHeadingFinish = doc.querySelector('#headingFinish button');
            if (headingFinish && docHeadingFinish) {
                headingFinish.innerHTML = docHeadingFinish.innerHTML;
            }

            const headingDownloads = document.querySelector('#headingDownloads button');
            const docHeadingDownloads = doc.querySelector('#headingDownloads button');
            if (headingDownloads && docHeadingDownloads) {
                headingDownloads.innerHTML = docHeadingDownloads.innerHTML;
            }
        })
        .catch(error => {
            console.error('Error updating file lists:', error);
            showStatus('Error updating file list: ' + error.message, 'danger');
        });
}