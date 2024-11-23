import streamlit as st

def calculate(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 == 0:
            return "Error: Division by zero is not allowed."
        return num1 / num2
    else:
        return "Invalid operation"

# Streamlit App Interface
st.title("Simple Calculator")
st.write("Enter two numbers and select an operation to calculate the result.")

# User inputs
num1 = st.number_input("Enter the first number:", step=1.0)
num2 = st.number_input("Enter the second number:", step=1.0)
operation = st.selectbox("Select an operation:", ("+", "-", "*", "/"))

# Calculate and display result when button is clicked
if st.button("Calculate"):
    result = calculate(num1, num2, operation)
    st.write(f"The result of {num1} {operation} {num2} is: {result}")
