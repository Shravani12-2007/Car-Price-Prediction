# pip install streamlit

import streamlit as st
import pandas as pd
import pickle as pkl

# Add Title to web 
st.title("Car Price Prediction App")

# # Load Cleaned Dataset
df = pd.read_csv("final_cleaned_dataset.csv")

# # Get unique values for add in dropbox
companies = sorted(df['company'].unique())
fuel_types = sorted(df['fuel_type'].unique())

# # Create a selectbox for comapnies
company = st.selectbox("Select Company", companies)

names = sorted(df[df['company'] == company]['name'].unique())

# # Create a selectbox for Names
name = st.selectbox("Select name", names)

# # Create a number input section for year
year = st.number_input("Enter year", min_value=1995, max_value=2024, value=2015, step=1)

# # Create a number input section for kms_driven
kms_driven = st.number_input("Enter kms driven", min_value=1000, max_value=4000000, value=50000, step=5000)

# # Create a select box for fuel_type
fuel_type = st.selectbox("Select fuel type", fuel_types)

# # Create a predict button
if st.button("Predict Price"):

#     # Take input values and convert it into dataframe
    myinput = pd.DataFrame(data = [[company, name, year, kms_driven, fuel_type]], columns = ['company', 'name', 'year', 'kms_driven', 'fuel_type'])

#     # Show input dataframe
    st.write("Input Data:")
    st.dataframe(myinput)

#     # Load trained model for prediction in rb mode
    model = pkl.load(open('model.pkl', 'rb'))

#     # Make prediction
    result = model.predict(myinput)

#     # show predicted value with green background
    st.success("Predicted price:" + str(round(result[0,0])))

# # streamlit run .\app.py