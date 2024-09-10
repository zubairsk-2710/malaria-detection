
<h1>Malaria Detection using Deep Learning 🦟🦠</h1>

<p align="center">
  <a href="https://github.com/zubairsk-2710/malaria-detection">
    <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTKmxwPwETBdFmjFSPAG1a6BS6L5-UFbDr18w&s" alt="Logo" width="150" height="150">
  </a>
</p>

<h2>📌 Introduction</h2>
<p>
  This web application utilizes Convolutional Neural Networks (CNNs) to detect malaria from blood cell images. 
  The model is capable of predicting whether the image shows an infected or uninfected cell, and if infected, 
  it can identify the stage of malaria. The project features a Flask-based web interface for easy interaction 
  and image upload.
</p>

<h2>🎯 Purpose of the Project</h2>
<p>
  Malaria remains a significant health concern in many regions. This tool aims to provide an easy-to-use web 
  application for detecting malaria from blood cell images. With an accuracy of approximately 95%, it assists 
  healthcare providers in diagnosing malaria efficiently.
</p>

<h2>🏁 Technology Stack</h2>
<ul>
  <li><a href="https://github.com/pallets/flask">Flask</a> - Web framework</li>
  <li><a href="https://www.tensorflow.org/">TensorFlow</a> - Machine learning library</li>
  <li><a href="https://keras.io/">Keras</a> - Deep learning API</li>
  <li><a href="https://numpy.org/">NumPy</a> - Numerical computing</li>
  <li><a href="http://www.h5py.org/">H5py</a> - HDF5 file handling</li>
</ul>

<h2>🔬 Algorithm Models</h2>
<p>
  The project utilizes several CNN architectures to classify blood cell images:
</p>
<ul>
  <li><b>VGG16:</b> A deep convolutional network with 16 layers, known for its simplicity and effectiveness in image classification tasks.</li>
  <li><b>VGG19:</b> An extension of VGG16 with 19 layers, offering improved performance through deeper architecture.</li>
  <li><b>ResNet:</b> A residual network that helps in training very deep networks by using skip connections to bypass certain layers.</li>
</ul>

<h2>🛠️ Installation</h2>
<ol>
  <li><b>Clone the Repository:</b></li>
  <pre><code>git clone https://github.com/zubairsk-2710/malaria-detection.git
cd malaria-detection</code></pre>

  <li><b>Create and Activate a Virtual Environment:</b></li>
  <pre><code>python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`</code></pre>

  <li><b>Install Dependencies:</b></li>
  <p>Create a <code>requirements.txt</code> file with the following content:</p>
  <pre><code>Flask==2.3.2
tensorflow==2.14.0
keras==2.15.0
numpy==1.23.4
h5py==3.8.0</code></pre>
  <p>Then install the dependencies:</p>
  <pre><code>pip install -r requirements.txt</code></pre>

  <li><b>Run the Application:</b></li>
  <pre><code>python app.py</code></pre>
  <p>Navigate to <a href="http://127.0.0.1:5000/">http://127.0.0.1:5000/</a> in your web browser to access the application.</p>
</ol>

<h2>🖥️ Usage</h2>
<ul>
  <li><b>Home Page:</b> Provides an overview and navigation to other sections of the application.</li>
  <li><b>Prediction Page:</b> Allows you to upload an image of a blood cell. The model will predict whether the cell is infected or uninfected, and if infected, identify the stage of malaria. The accuracy of the prediction is also shown.</li>
  <li><b>Contact Page:</b> Contains contact information for further inquiries.</li>
  <li><b>About Us Page:</b> Provides information about the project and its objectives.</li>
  <li><b>Chatbot Page:</b> Features a basic chatbot interface for user interaction.</li>
</ul>

<h2>📋 Further Improvements</h2>
<ul>
  <li>Deploying the web application on a cloud platform.</li>
  <li>Enhancing the user interface with additional features and styling.</li>
  <li>Containerizing the application using Docker.</li>
</ul>

<h2>📜 License</h2>
<p>
  This project is licensed under the <a href="LICENSE">MIT License</a>.
</p>
