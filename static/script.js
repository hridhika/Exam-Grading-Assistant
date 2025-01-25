document.addEventListener('DOMContentLoaded', function () {
    const uploadButton = document.querySelector('.upload-button');
    const fileInput = document.createElement('input');
    fileInput.type = 'file';
    fileInput.accept = 'image/*';

    const progressBarContainer = document.createElement('div');
    progressBarContainer.style.position = 'relative';
    progressBarContainer.style.width = '100%';
    progressBarContainer.style.height = '10px';
    progressBarContainer.style.backgroundColor = '#f0f0f0';
    progressBarContainer.style.borderRadius = '5px';
    progressBarContainer.style.marginTop = '15px';
    progressBarContainer.style.display = 'none';

    const progressBar = document.createElement('div');
    progressBar.style.height = '100%';
    progressBar.style.width = '0%';
    progressBar.style.backgroundColor = '#4CAF50';
    progressBar.style.borderRadius = '5px';
    progressBar.style.transition = 'width 0.3s';

    progressBarContainer.appendChild(progressBar);
    document.querySelector('.upload-section').appendChild(progressBarContainer);

    uploadButton.addEventListener('click', function () {
        fileInput.click();
    });

    function updateProgress(percentage) {
        progressBar.style.width = `${percentage}%`;
    }

    function processUpload(file) {
        const formData = new FormData();
        formData.append('file', file);

        progressBarContainer.style.display = 'block';
        updateProgress(0);

        fetch('/upload', {
            method: 'POST',
            body: formData,
        })
            .then((response) => {
                if (!response.ok) {
                    throw new Error('Failed to upload');
                }
                return response.json();
            })
            .then((data) => {
                // Store results in localStorage for results page
                localStorage.setItem(
                    'examResults',
                    JSON.stringify({
                        extractedText: data.extracted_text,
                        referenceAnswer: data.reference_answer,
                        similarityScore: data.similarity_score,
                        isCorrect: data.is_correct,
                    })
                );

                // Simulate completion progress
                updateProgress(100);

                setTimeout(() => {
                    // Redirect to results page
                    window.location.href = '/results';
                }, 500); // Add a slight delay for better UX
            })
            .catch((error) => {
                console.error('Error:', error);
                alert('Failed to upload and grade image');
                progressBarContainer.style.display = 'none';
            });
    }

    fileInput.addEventListener('change', function (event) {
        const file = event.target.files[0];
        if (file) {
            processUpload(file);
        }
    });

    // Drag and drop functionality
    const uploadSection = document.querySelector('.upload-section');

    uploadSection.addEventListener('dragover', function (e) {
        e.preventDefault();
        uploadSection.style.backgroundColor = '#D9AEDC';
    });

    uploadSection.addEventListener('dragleave', function (e) {
        e.preventDefault();
        uploadSection.style.backgroundColor = '#EAF0FA';
    });

    uploadSection.addEventListener('drop', function (e) {
        e.preventDefault();
        uploadSection.style.backgroundColor = '#EAF0FA';

        const file = e.dataTransfer.files[0];
        if (file) {
            processUpload(file);
        }
    });
});
