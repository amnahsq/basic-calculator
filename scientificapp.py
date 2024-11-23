import streamlit as st
import math

# Application Title
st.title("Scientific Calculator")

# Input section
st.header("Input")
num1 = st.number_input("Enter the first number", value=0.0)
num2 = st.number_input("Enter the second number (if required)", value=0.0)

# Select operation
st.header("Operations")
operation = st.selectbox(
    "Select an operation",
    [
        "Addition",
        "Subtraction",
        "Multiplication",
        "Division",
        "Square Root",
        "Power",
        "Logarithm",
        "Sine",
        "Cosine",
        "Tangent"
    ]
)

# Calculate result based on operation
st.header("Result")
if st.button("Calculate"):
    try:
        if operation == "Addition":
            result = num1 + num2
            st.success(f"The result is: {result}")
        elif operation == "Subtraction":
            result = num1 - num2
            st.success(f"The result is: {result}")
        elif operation == "Multiplication":
            result = num1 * num2
            st.success(f"The result is: {result}")
        elif operation == "Division":
            if num2 != 0:
                result = num1 / num2
                st.success(f"The result is: {result}")
            else:
                st.error("Error: Division by zero")
        elif operation == "Square Root":
            if num1 >= 0:
                result = math.sqrt(num1)
                st.success(f"The result is: {result}")
            else:
                st.error("Error: Negative input for square root")
        elif operation == "Power":
            result = math.pow(num1, num2)
            st.success(f"The result is: {result}")
        elif operation == "Logarithm":
            if num1 > 0:
                result = math.log(num1, num2 if num2 > 0 else math.e)
                st.success(f"The result is: {result}")
            else:
                st.error("Error: Logarithm base and argument must be positive")
        elif operation == "Sine":
            result = math.sin(math.radians(num1))
            st.success(f"The result is: {result}")
        elif operation == "Cosine":
            result = math.cos(math.radians(num1))
            st.success(f"The result is: {result}")
        elif operation == "Tangent":
            result = math.tan(math.radians(num1))
            st.success(f"The result is: {result}")
        else:
            st.error("Invalid operation selected")
    except Exception as e:
        st.error(f"An error occurred: {e}")

