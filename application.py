from flask import Flask, request, render_template
import numpy as np
import pandas as pd
import os  # Ensure 'os' is imported

from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

application = Flask(__name__)

app=application

# Route for the main index page
@app.route('/')
def index():
    return render_template('index.html')

# Route for the prediction form
@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        try:
            # Correctly map form data to CustomData parameters
            data = CustomData(
                gender=request.form.get('gender'),
                race_ethnicity=request.form.get('ethnicity'),
                parental_level_of_education=request.form.get('parental_level_of_education'),
                lunch=request.form.get('lunch'),
                test_preparation_course=request.form.get('test_preparation_course'),
                reading_score=float(request.form.get('reading_score')),
                writing_score=float(request.form.get('writing_score'))
            )
            
            pred_df = data.get_data_as_data_frame()
            print("Received data from form:", pred_df)

            predict_pipeline = PredictPipeline()
            results = predict_pipeline.predict(pred_df)
            
            print("Prediction result:", results)

            # Pass the prediction result to the HTML template
            return render_template('home.html', results=results[0])
            
        except Exception as e:
            # Handle potential errors during prediction
            print(f"Error during prediction: {e}")
            return render_template('home.html', results="Error during prediction")

if __name__ == "__main__":
    app.run(host="0.0.0.0")
