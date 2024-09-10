# malaria-detection
Malaria Detection using Deep Learning 🦟🦠
<p align="center"> <a href="https://github.com/zubairsk-2710/malaria-detection"> <img src="https://pngimage.net/wp-content/uploads/2018/06/malaria-in-png-1.png" alt="Logo" width="150" height="150"> </a> </p>
📌 Introduction
This web application utilizes Convolutional Neural Networks (CNNs) to detect malaria from blood cell images. The model is capable of predicting whether the image shows an infected or uninfected cell, and if infected, it can identify the stage of malaria. The project features a Flask-based web interface for easy interaction and image upload.

🎯 Purpose of the Project
Malaria remains a significant health concern in many regions. This tool aims to provide an easy-to-use web application for detecting malaria from blood cell images. With an accuracy of approximately 95%, it assists healthcare providers in diagnosing malaria efficiently.

🏁 Technology Stack
Flask - Web framework
TensorFlow - Machine learning library
Keras - Deep learning API
NumPy - Numerical computing
H5py - HDF5 file handling
🔬 Algorithm Models
The project utilizes several CNN architectures to classify blood cell images:

VGG16: A deep convolutional network with 16 layers, known for its simplicity and effectiveness in image classification tasks.
VGG19: An extension of VGG16 with 19 layers, offering improved performance through deeper architecture.
ResNet: A residual network that helps in training very deep networks by using skip connections to bypass certain layers.
🛠️ Installation
Clone the Repository:

bash
Copy code
git clone https://github.com/zubairsk-2710/malaria-detection.git
cd malaria-detection
Create and Activate a Virtual Environment:

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install Dependencies:

Create a requirements.txt file with the following content:

plaintext
Copy code
Flask==2.3.2
tensorflow==2.14.0
keras==2.15.0
numpy==1.23.4
h5py==3.8.0
Then install the dependencies:

bash
Copy code
pip install -r requirements.txt
Run the Application:

bash
Copy code
python app.py
Navigate to http://127.0.0.1:5000/ in your web browser to access the application.

🖥️ Usage
Home Page: Provides an overview and navigation to other sections of the application.
Prediction Page: Allows you to upload an image of a blood cell. The model will predict whether the cell is infected or uninfected, and if infected, identify the stage of malaria. The accuracy of the prediction is also shown.
Contact Page: Contains contact information for further inquiries.
About Us Page: Provides information about the project and its objectives.
Chatbot Page: Features a basic chatbot interface for user interaction.
📋 Further Improvements
 Deploying the web application on a cloud platform.
 Enhancing the user interface with additional features and styling.
 Containerizing the application using Docker.
📜 License
This project is licensed under the MIT License.
