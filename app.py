import streamlit as st
import pandas as pd
import joblib
from datetime import date

# Page configuration
st.set_page_config(
    page_title="HHS Care Load Forecasting",
    page_icon="📊",
    layout="centered"
)

# Title
st.title("📊 HHS Care Load Forecasting")

st.write(
    "This application predicts the number of children in HHS care "
    "using a Random Forest Regression model."
)

st.divider()

# Load trained model
@st.cache_resource
def load_model():
    return joblib.load("models/random_forest_hhs_care_model.pkl")

model = load_model()

# Date input
st.subheader("Enter Prediction Date")

selected_date = st.date_input(
    "Select a date",
    value=date.today()
)

# Extract date features
year = selected_date.year
month = selected_date.month
day = selected_date.day
dayofweek = selected_date.weekday()
dayofyear = selected_date.timetuple().tm_yday

# Create input data
input_data = pd.DataFrame({
    "year": [year],
    "month": [month],
    "day": [day],
    "dayofweek": [dayofweek],
    "dayofyear": [dayofyear]
})

# Show extracted features
st.subheader("Date Features")

st.dataframe(
    input_data,
    use_container_width=True
)

# Prediction button
if st.button("🔮 Predict Care Load", use_container_width=True):

    prediction = model.predict(input_data)

    predicted_value = prediction[0]

    st.success(
        f"Predicted number of children in HHS care: "
        f"{predicted_value:.0f}"
    )

    st.info(
        "Prediction generated using the trained Random Forest model."
    )

st.divider()

st.caption(
    "Machine Learning Project | Random Forest Regression"
)