# Import libraries
import streamlit as st
import pandas as pd
import numpy as np
from tensorflow.keras.models import load_model

# Load the trained model
model = load_model('churning_data.h5')

def main():
    st.title("Customer Churn App")
    st.warning("Provide customer details to predict customer churn.")

    # User inputs
    gender = st.selectbox(' Customer gender:', ['female', 'male'])
    SeniorCitizen = st.selectbox(' Is customer a senior citizen:', [0, 1])
    Partner = st.selectbox('Partner:', ['yes', 'no'])
    PaperlessBilling = st.selectbox('PaperlessBilling:', ['yes', 'no'])

    # Convert categorical values to numerical values
    gender = 1 if gender == 'male' else 0
    Partner = 1 if Partner == 'yes' else 0
    PaperlessBilling = 1 if PaperlessBilling == 'yes' else 0

    # Convert "TechSupport" categorical value to numerical
    TechSupport_mapping = {'no': 0, 'yes': 1, 'no internet service': 2}
    TechSupport = st.selectbox('TechSupport:', list(TechSupport_mapping.keys()))
    TechSupport = TechSupport_mapping[TechSupport] 

    # Convert "DeviceProtection" categorical value to numerical
    DeviceProtection_mapping = {'no': 0, 'yes': 1, 'no internet service': 2}
    DeviceProtection = st.selectbox('DeviceProtection:', list(DeviceProtection_mapping.keys()))
    DeviceProtection = DeviceProtection_mapping[DeviceProtection]

    # Convert "InternetService" categorical value to numerical
    InternetService_mapping = {'DSL': 0, 'Fiber optic': 1, 'no': 2}
    InternetService = st.selectbox('InternetService:', list(InternetService_mapping.keys()))
    InternetService = InternetService_mapping[InternetService]
    
    # Convert "MultipleLines" categorical value to numerical
    MultipleLines_mapping = {'no': 0, 'yes': 1, 'no phone service': 2}
    MultipleLines = st.selectbox('MultipleLines:', list(MultipleLines_mapping.keys()))
    MultipleLines = MultipleLines_mapping[MultipleLines] 

    # Convert "OnlineBackup" categorical value to numerical
    OnlineBackup_mapping = {'no': 0, 'yes': 1, 'no internet service': 2}
    OnlineBackup = st.selectbox('OnlineBackup:', list(OnlineBackup_mapping.keys()))
    OnlineBackup = OnlineBackup_mapping[OnlineBackup] 

    # Convert "OnlineSecurity" categorical value to numerical
    OnlineSecurity_mapping = {'no': 0, 'yes': 1, 'no internet service': 2}
    OnlineSecurity = st.selectbox('OnlineSecurity:', list(OnlineSecurity_mapping.keys()))
    OnlineSecurity = OnlineSecurity_mapping[OnlineSecurity]

    # Convert "PaymentMethod" categorical value to numerical
    PaymentMethod_mapping = {'Bank transfer (automatic)': 0, 'Credit card (automatic)': 1, 'Electronic check': 2, 'Mailed check':3}
    PaymentMethod = st.selectbox('PaymentMethod:', list(PaymentMethod_mapping.keys()))
    PaymentMethod = PaymentMethod_mapping[PaymentMethod]

    # Convert "Contract" categorical value to numerical
    contract_mapping = {'month-to-month': 0, 'one_year': 1, 'two_years': 2}
    Contract = st.selectbox('Contract:', list(contract_mapping.keys()))
    Contract = contract_mapping[Contract]
    
    tenure = st.number_input('tenure (How many months has customer associated with the organization):', min_value=0, max_value=24, value=0)
    MonthlyCharges = st.number_input('Monthly charges:', min_value=0, max_value=90, value=0)
    TotalCharges = tenure * MonthlyCharges

    # Display TotalCharges
    st.warning(f'TotalCharges: {TotalCharges}')

    #  Make prediction when the user clicks the button
    if st.button('Predict Churn'):
        features = model.predict([[gender, SeniorCitizen, Partner, MultipleLines, InternetService, OnlineSecurity, OnlineBackup, DeviceProtection, TechSupport, PaperlessBilling, Contract, tenure, MonthlyCharges,PaymentMethod, TotalCharges]])
        predict = np.round(features[0],2)
        st.success(f"Customer Churn Probability: {predict}")


        if predict >= 0.5:
            st.warning("Customer will  churn.")
        else:
            st.warning("Customer will not churn.")

        # Calculate confidence factor
        confidence_factor = 2.58 * np.sqrt((predict * (1 - predict)) / 1) 
        st.write(f"Confidence Factor: {confidence_factor}")


if __name__ == "__main__":
    main()