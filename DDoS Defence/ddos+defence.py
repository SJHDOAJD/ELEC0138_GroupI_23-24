from flask import Flask, request, jsonify, render_template
import tensorflow as tf
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler, LabelEncoder
from sklearn.impute import SimpleImputer
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

# Load the model
model = tf.keras.models.load_model("DNN_model.h5")

# Data preprocessing tools
scaler = MinMaxScaler()
label_encoders = {}  # Dictionary to store label encoders for each categorical column

# Ensure a folder for uploaded files is available
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Check if the post request has the file part
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'})
    
    if file:
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        
        # Read data from CSV
        input_df = pd.read_csv(file_path)

        # Handle categorical and missing data
        for column in input_df.columns:
            if input_df[column].dtype == 'object':
                if column not in label_encoders:
                    le = LabelEncoder()
                    input_df[column] = le.fit_transform(input_df[column].astype(str))
                    label_encoders[column] = le
                else:
                    le = label_encoders[column]
                    input_df[column] = le.transform(input_df[column].astype(str))
            else:
                imputer = SimpleImputer(strategy='mean')
                input_df[column] = imputer.fit_transform(input_df[[column]])

        # Encode and scale data
        input_scaled = scaler.fit_transform(input_df)
        
        # Use model to make predictions
        prediction = model.predict(input_scaled)
        prediction = (prediction > 0.5).astype(int)
        
        # Determine result
        result = ["DDOS Attack" if pred == 1 else "Normal" for pred in prediction.flatten()]

        # Remove the uploaded file after processing (optional)
        os.remove(file_path)
        
        return jsonify({'predictions': result})

if __name__ == "__main__":
    app.run(debug=True)
