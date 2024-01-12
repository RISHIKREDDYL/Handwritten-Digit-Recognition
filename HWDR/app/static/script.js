function predict() {
    var fileInput = document.getElementById('file-input');
    var file = fileInput.files[0];

    if (!file) {
        alert("Please select an image file.");
        return;
    }

    var formData = new FormData();
    formData.append('file', file);

    fetch('/predict', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            console.error('Error:', data.error);
        } else {
            var predictionContainer = document.getElementById('prediction-container');
            predictionContainer.innerHTML = '<h2>Prediction: ' + data.prediction + '</h2>';
        }
    })
    .catch(error => console.error('Error:', error));
}