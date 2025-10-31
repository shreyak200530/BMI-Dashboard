import streamlit as st

# --- Title and Description ---
st.title("🧮 BMI Calculator")
st.write("Calculate your Body Mass Index (BMI) using height and weight.")

# --- Sidebar Inputs ---
st.sidebar.header("Enter your details")

height_cm = st.sidebar.slider("Height (cm)", min_value=100, max_value=250, value=170)
weight_kg = st.sidebar.slider("Weight (kg)", min_value=30, max_value=200, value=70)

# --- BMI Calculation ---
height_m = height_cm / 100
bmi = round(weight_kg / (height_m ** 2), 2)

# --- Display Results ---
st.subheader("Your Results")
st.write(f"*Height:* {height_cm} cm")
st.write(f"*Weight:* {weight_kg} kg")
st.write(f"*BMI:* {bmi}")

# --- BMI Category ---
if bmi < 18.5:
    category = "Underweight"
    st.warning(f"Category: {category}")
elif 18.5 <= bmi < 24.9:
    category = "Normal weight"
    st.success(f"Category: {category}")
elif 25 <= bmi < 29.9:
    category = "Overweight"
    st.info(f"Category: {category}")
else:
    category = "Obese"
    st.error(f"Category: {category}")

# --- Footer ---
st.markdown("---")
st.caption("BMI is a general indicator. Always consult a healthcare professional for personalized advice.")