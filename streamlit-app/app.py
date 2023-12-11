import streamlit as st
#import openai 
#from openai import OpenAI

st.write("hi world!")

def BMI_calc(w, h): 
    bmi = (w/(h**2))*703
    return bmi 

#BMI calculator 
weight = st.number_input("Enter your weight in lbs", min_value= 0.1)
height = st.number_input("Enter your height in inches")
if st.button("click here to calculate BMI"):
    bmi = BMI_calc(weight, height)
    st.write(bmi)


