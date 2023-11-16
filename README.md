# Customer Churn Prediction App

## Overview

This is a Streamlit web application that predicts customer churn based on a trained machine-learning model. The model has been developed using a dataset containing customer information.

## Usage

1. **Run the App:**
    - Ensure you have Python installed on your machine.
    - Install the required libraries by running `pip install -r requirements.txt` in your terminal.
    - Run the app using `streamlit run app.py`.

2. **Input Customer Details:**
    - Select customer gender, senior citizen status, partner status, paperless billing status, and other relevant information.

3. **Make a Prediction:**
    - Click the "Predict Churn" button to make a prediction.
    - The app will display the customer churn probability and whether the customer is likely to churn or not.

4. **Confidence Factor:**
    - The confidence factor is also displayed, indicating the level of confidence in the prediction.

## Files and Structure

- `app.py`: Contains the Streamlit web application code.
- `churning_data.h5`: Contains the Trained machine learning model file.


## Data and Model

- The machine learning model was trained using a dataset located at `/content/drive/MyDrive/colab labs/CustomerChurn_dataset.csv`.
- The model uses a neural network architecture developed with the TensorFlow and Keras libraries.

## Additional Information

- For more details on the model, data preprocessing, and exploratory data analysis, refer to the original notebook: [92642023_Churning_Customers.ipynb]

## Author

Winifred Adjei

## Link to video demonstrating my model deployment-> https://youtu.be/8DG6iZM403s


