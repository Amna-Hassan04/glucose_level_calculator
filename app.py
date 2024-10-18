import streamlit as st

# Function to calculate estimated HbA1c from average glucose level
def calculate_hba1c(avg_glucose):
    # Formula to estimate HbA1c from average glucose levels
    return (avg_glucose + 46.7) / 28.7

# Function to provide health advice based on glucose level
def glucose_health_advice(glucose):
    if glucose < 70:
        return "Your blood sugar is too low. You may be experiencing hypoglycemia."
    elif 70 <= glucose <= 99:
        return "Your blood sugar is normal."
    elif 100 <= glucose <= 125:
        return "You may have prediabetes. Consider a healthy lifestyle and consult a doctor."
    elif glucose > 125:
        return "Your blood sugar is high. You may have diabetes. Please consult a healthcare provider."
    else:
        return "Invalid glucose level."

# Title
st.title("Blood Glucose Level Assessment and HbA1c Estimation")

# Input: User enters their blood glucose level
glucose = st.number_input("Enter your fasting blood glucose level (mg/dL):", min_value=1)

# Display estimated HbA1c and health advice
if glucose:
    hba1c = calculate_hba1c(glucose)
    advice = glucose_health_advice(glucose)
    
    # Show results
    st.subheader("Estimated HbA1c")
    st.write(f"Your estimated HbA1c is: **{hba1c:.2f}%**")
    
    st.subheader("Health Advice")
    st.write(advice)

# Add some additional information
st.info("The HbA1c is an estimate based on your average glucose levels over time. Consult with a healthcare professional for an accurate diagnosis.")
