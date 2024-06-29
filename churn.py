# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 22:26:17 2024

@author: Fatima
"""

import pandas as pd
import streamlit as st
import pickle
#import xgboost as xgb

filename = 'finalxgb_model.sav'
model = pickle.load(open(filename, 'rb'))

st.title('Churn Prediction App')
st.subheader("""This app takes in certain variables to enable prediction whether or not a customer churned""")

def user_input():
    gender = st.selectbox('What is your gender', options=['Male', 'Female'], index=0)
    SeniorCitizen = st.selectbox('Are you a Senior citizen', options=['Yes', 'No'], index=0)
    Partner = st.selectbox('Do you have a Partner', options=['Yes', 'No'], index=0)
    Dependents = st.selectbox('Are you Dependents', options=['Yes', 'No'], index=0)
    tenure = st.number_input('How many tenure are you on', min_value=5.00, max_value=72.00)
    PhoneService = st.selectbox('Do you posess a Phone Service', options=['Yes', 'No'], index=0)
    MultipleLines = st.selectbox('Do you have Multiple Lines', options=['No phone service', 'Yes','No'],index=0)
    InternetService = st.selectbox('What type of Internet Service do you use', options=['No','DSL','Fiber optics'], index=0)
    OnlineSecurity = st.selectbox('Do you have Online Security', options=['No internet service', 'Yes', 'No'], index=0)
    OnlineBackup = st.selectbox('Do you have Online Backup', options=['No internet service', 'Yes', 'No'], index=0)
    DeviceProtection = st.selectbox('Is there a Device protection connected to your internet sevice',options=['No internet service','Yes', 'No'], index=0)
    TechSupport = st.selectbox('Do you have internet for Tech Support', options=['No internet service', 'Yes', 'No'], index=0)
    StreamingTV = st.selectbox('DO you Stream on TV', options=['No internet service', 'Yes', 'No'], index=0)
    StreamingMovies = st.selectbox('Are you streming movies', options=['No internet service', 'Yes', 'No'], index=0)
    Contract = st.selectbox('What type of contract are you subscribed to', options=['Month-to-month', 'One year', 'Two years'], index=0)
    PaperlessBilling = st.selectbox('Are you into PaperlessBilling', options=['Yes','No'], index =0)
    PaymentMethod = st.selectbox('What type of payment method would you use', options=['Bank transfer','Mailed check', 'Credit card'])
    MonthlyCharges = st.number_input('What is your monthly charges?', min_value=28.14, max_value=116.96)
    TotalCharges = st.number_input('What is the total charges', min_value=470.00, max_value= 7300.83)

    
    # Map 'Male' to 1 and 'Female' to 0
    gender_mapping = {'Male': 1, 'Female': 0}
    SeniorCitizen_mapping = {'Yes': 1, 'No': 0}
    Partner_mapping = {'Yes': 1, 'No': 0}
    Dependents_mapping ={'Yes': 1, 'No': 0}
    PhoneService_mapping = {'Yes': 1, 'No': 0}
    MultipleLines_mapping = {'No phone service': 1, 'Yes': 2, 'No': 0}
    InternetService_mapping = {'DSL': 0, 'Fiber optics': 1, 'No': 2}
    OnlineSecurity_mapping = {'No internet service': 1, 'Yes': 2, 'No': 0}
    OnlineBackup_mapping = {'No internet service': 1, 'Yes': 2, 'No': 0}
    DeviceProtection_mapping = {'No internet service': 1, 'Yes': 2, 'No': 0}
    TechSupport_mapping = {'No internet service': 1, 'Yes': 2, 'No': 0}
    StreamingTV_mapping = {'No internet service': 1, 'Yes': 2, 'No': 0}
    StreamingMovies_mapping = {'No internet service': 1, 'Yes': 2, 'No': 0}
    Contract_mapping = {'Month-to-month': 1, 'One year': 2, 'Two years':0}
    PaperlessBilling_mapping = {'Yes': 1, 'No': 0}
    PaymentMethod_mapping = {'Bank transfer': 1,'Mailed check': 0, 'Credit card': 2}
    
    
    
    data = {
        'gender': gender_mapping[gender],
        'SeniorCitizen':  SeniorCitizen_mapping[SeniorCitizen],
        'Partner': Partner_mapping[Partner],
        'Dependents': Dependents_mapping[Dependents],
        'tenure' : tenure,
        'PhoneService' : PhoneService_mapping[PhoneService],
        'MultipleLines' :  MultipleLines_mapping[MultipleLines],
        'InternetService' : InternetService_mapping[InternetService],
        'OnlineSecurity' : OnlineSecurity_mapping[OnlineSecurity],
        'OnlineBackup' : OnlineBackup_mapping[OnlineBackup],
        'DeviceProtection' : DeviceProtection_mapping[DeviceProtection],
        'TechSupport' : TechSupport_mapping[TechSupport],
        'StreamingTV' : StreamingTV_mapping[StreamingTV],
        'StreamingMovies': StreamingMovies_mapping[StreamingMovies],
        'Contract' : Contract_mapping[Contract],
        'PaperlessBilling' : PaperlessBilling_mapping[PaperlessBilling],
        'PaymentMethod' : PaymentMethod_mapping[PaymentMethod],
        'MonthlyCharges': MonthlyCharges,
        'TotalCharges': TotalCharges
    }
    
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input()

def prediction():
    predict_ = model.predict(df)
    result = ''
    if predict_ == 0:
        result = 'likely to continue patronizing your business.'
    else:
        result = 'likely to stop patronizing your business.'
    return result

# Prediction button
if st.button("Predict"):
    result = prediction()
    st.success('Thank you for filling this form. This Customer is {}'.format(result))
