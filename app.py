# from flask import Flask, request, jsonify, render_template
# import os
# from flask_cors import CORS, cross_origin
# from cnnClassifier.utils.common import decodeImage
# from cnnClassifier.pipeline.predict import PredictionPipeline

# os.putenv('LANG', 'en_US.UTF-8')
# os.putenv('LC_ALL', 'en_US.UTF-8')

# app = Flask(__name__)
# CORS(app)

# clApp = ClientApp()  # <-- create here globally

# class ClientApp:
#     def __init__(self):
#         self.filename = "inputImage.jpg"
#         self.classifier = PredictionPipeline(self.filename)

# @app.route("/", methods=['GET'])
# @cross_origin()
# def home():
#     return render_template('index.html')

# @app.route("/train", methods=['GET','POST'])
# @cross_origin()
# def trainRoute():
#     os.system("python main.py")
#     return "Training done successfully!"

# @app.route("/predict", methods=['POST'])
# @cross_origin()
# def predictRoute():
#     image = request.json['image']
#     decodeImage(image, clApp.filename)
#     result = clApp.classifier.predict()
#     return jsonify(result)

# if __name__ == "__main__":
#     # app.run(host='0.0.0.0', port=8080) #local host
#     app.run(host='0.0.0.0', port=8080) #for AWS
#     # app.run(host='0.0.0.0', port=80) #for AZURE

# app.py
import streamlit as st
from cnnClassifier.pipeline.predict import PredictionPipeline
from cnnClassifier.utils.common import decodeImage
import base64
import os

st.title("🐔 Chicken Disease Classification")

uploaded_file = st.file_uploader("Upload an image of a chicken", type=['jpg', 'jpeg', 'png'])

if uploaded_file is not None:
    image_bytes = uploaded_file.read()
    with open("inputImage.jpg", "wb") as f:
        f.write(image_bytes)
    
    st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)

    if st.button("Classify"):
        pipeline = PredictionPipeline("inputImage.jpg")
        result = pipeline.predict()
        st.success(f"Prediction: {result}")
