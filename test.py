import streamlit as st

# Title of the Streamlit app
st.title("Add Two Numbers")

# Input fields to enter two numbers
num1 = st.number_input("Enter the first number", value=0)
num2 = st.number_input("Enter the second number", value=0)

# Button to perform addition
if st.button("Add"):
    result = num1 + num2
    st.write(f"The result of {num1} + {num2} is: {result}")
