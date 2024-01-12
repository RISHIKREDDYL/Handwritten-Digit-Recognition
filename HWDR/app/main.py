import os
from flask import Flask, render_template, request, redirect, url_for, jsonify
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from io import BytesIO
import numpy as np

app = Flask(__name__)

model_path = os.path.join(os.path.dirname(__file__), '..', 'model', 'LeNet.h5')
model = load_model(model_path)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        if 'file' not in request.files:
            return jsonify({'error': 'No file part'})

        file = request.files['file']

        if file.filename == '':
            return jsonify({'error': 'No selected file'})

        img_bytes = BytesIO(file.read())
        img = image.load_img(img_bytes, target_size=(32, 32))
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0) / 255.0

        prediction = model.predict(img_array)
        predicted_class = int(np.argmax(prediction))

        return jsonify({'prediction': predicted_class})

    return jsonify({'error': 'Unsupported method'})

if __name__ == '__main__':
    app.run(debug=True)