import streamlit as st

# Function to perform calculations
def calculate(operation, num1, num2):
    if operation == 'Add':
        return num1 + num2
    elif operation == 'Subtract':
        return num1 - num2
    elif operation == 'Multiply':
        return num1 * num2
    elif operation == 'Divide':
        return num1 / num2 if num2 != 0 else 'Error (Division by 0)'

# Main app
def main():
    st.markdown("<h1 style='text-align: center; color: #4CAF50;'>Calculator</h1>", unsafe_allow_html=True)

    st.markdown(
        """
        <style>
        .stApp {
            background-color: #f0f5f5;
            border-radius: 10px;
            padding: 20px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    st.write("Enter two numbers and select an operation to calculate.")

    # Input fields
    num1 = st.number_input("Enter the first number", min_value=None, step=1.0, format="%.2f")
    num2 = st.number_input("Enter the second number", min_value=None, step=1.0, format="%.2f")

    # Dropdown menu for operations
    operation = st.selectbox("Choose an operation", ('Add', 'Subtract', 'Multiply', 'Divide'))

    # Calculate button
    if st.button("Calculate"):
        result = calculate(operation, num1, num2)
        st.markdown(f"<h3 style='text-align: center; color: #FF6347;'>Result: {result}</h3>", unsafe_allow_html=True)

# Running the app
if __name__ == '__main__':
    main()
