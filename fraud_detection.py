import streamlit as st
import pandas as pd
import joblib

model = joblib.load('fraud_detection_pipeline.pkl')
st.title('Fraud Detection Prediction App')
st.markdown('Please enter the transaction details and use the Predict button')
st.divider()

transaction_type = st.selectbox('Transaction Type',['PAYMENT', 'TRANSFER', 'CASH_OUT', 'DEPOSIT'])
amount = st.number_input('Amount', min_value=0.0, value=1000.0)
oldbalanceOrg = st.number_input('oldbalanceOrg (Sender)', min_value=0.0, value=10000.0)
newbalanceOrig = st.number_input('newbalanceOrig (Sender)', min_value=0.0, value=9000.0)
oldbalanceDet = st.number_input('oldbalanceDest (Receiver)', min_value=0.0, value=0.0)
newbalanceDest = st.number_input('newbalanceDest (Receiver)', min_value=0.0, value=0.0)

# defining prediction button
if st.button('Predict'):
    input_data = pd.DataFrame([{
        'type': transaction_type,
        'amount': amount,
        'oldbalanceOrg': oldbalanceOrg,
        'newbalanceOrig': newbalanceOrig,
        'oldbalanceDest': oldbalanceDet,
        'newbalanceDest': newbalanceDest
    }])

    prediction = model.predict(input_data)[0]

    st.subheader(f"Prediction: '{int(prediction)}'")

    if prediction == 1:
        st.error('The transaction is predicted to be FRAUDULENT.')
    else:
        st.success('The transaction is predicted to be LEGITIMATE.')

