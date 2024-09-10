from flask import Flask, render_template, request, jsonify
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model
import numpy as np
import os
import io

app = Flask(__name__)
model = load_model("model.h5")

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('/home.html')
@app.route('/about')
def about():
    return render_template('/about.html')
@app.route('/contact')
def contact():
    return render_template('/contact.html')
@app.route('/index')
def home():
    return render_template('/index.html')
@app.route('/chatbot')
def chatbot():
    return render_template('/chatbot.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    if not allowed_file(file.filename):
        return jsonify({'error': 'Invalid file format'})

    try:
        # Convert file storage object to bytes-like object
        img_bytes = io.BytesIO()
        file.save(img_bytes)
        img_bytes.seek(0)

        img = image.load_img(img_bytes, target_size=(100, 100))
        img_tensor = image.img_to_array(img)
        img_tensor = np.expand_dims(img_tensor, axis=0)
        img_tensor /= 255.0

        prediction = model.predict(img_tensor)[0][0]
        predicted_class = "Uninfected" if prediction >= 0.5 else "Parasitized"
        confidence = float(prediction)

        # Assuming you have the actual label in actual_label variable
        actual_label = "Parasitized"  # You need to set this based on your data
        
        # Calculate accuracy
        accuracy = 100 if predicted_class == actual_label else 0  # You need to implement the actual accuracy calculation
        
        return jsonify({'prediction': predicted_class, 'confidence': confidence * 100, 'accuracy': accuracy})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
