import streamlit as st

st.title('BMI Calculator')

weight = st.number_input('Enter your weight (kg):', min_value=1.0, step=0.1)
height = st.number_input('Enter your height (m):', min_value=0.1, step=0.01)

if weight > 0 and height > 0:
    bmi = weight / (height ** 2)
    st.write(f'Your BMI is: {bmi:.2f}')
    
    # Provide BMI category
    if bmi < 18.5:
        st.write('Category: Underweight')
    elif 18.5 <= bmi < 24.9:
        st.write('Category: Normal weight')
    elif 25 <= bmi < 29.9:
        st.write('Category: Overweight')
    else:
        st.write('Category: Obesity')
else:
    st.write('Please enter valid weight and height.')
