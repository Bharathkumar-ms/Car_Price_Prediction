import streamlit as st
from car.pipeline.prediction import CustomData, PredictPipeline

# Create a Streamlit web app
st.title('Car Price Prediction')

# Define input fields
present_price = st.number_input('Present Price', min_value=0.0)
kms_driven = st.number_input('Kilometers Driven', min_value=0.0)
owner = st.number_input('Owner', min_value=0.0)
age = st.number_input('Age', min_value=0.0)

fuel_type = st.selectbox('Fuel Type', ['Petrol', 'Diesel', 'CNG'])
seller_type = st.selectbox('Seller Type', ['Dealer', 'Individual'])
transmission = st.selectbox('Transmission', ['Manual', 'Automatic'])

# Create a custom data object
data = CustomData(
    Present_Price=present_price,
    Kms_Driven=kms_driven,
    Owner=owner,
    age=age,
    Fuel_Type=fuel_type,
    Seller_Type=seller_type,
    Transmission=transmission
)

# Predict car price
if st.button('Predict Price'):
    pred_df = data.get_data_as_data_frame()

    predict_pipeline = PredictPipeline()
    results = predict_pipeline.predict(pred_df)

    # Display the prediction result
    st.subheader('Prediction Result')
    st.write(f'Predicted Price: {results[0]:.2f} INR')

