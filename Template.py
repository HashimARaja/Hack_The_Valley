# app.py

import streamlit as st
import pandas as pd
import numpy as np

# Set the title of the app
st.title("Welcome to My Streamlit App")

# Add a header
st.header("An Interactive Web Application")

# Add some text
st.write("This is a simple Streamlit app that demonstrates basic features.")

# Create a sidebar
st.sidebar.title("Sidebar Menu")
st.sidebar.write("You can add inputs here.")

# Add a slider to the sidebar
slider_value = st.sidebar.slider("Select a number", 0, 100, 50)

# Display the slider value
st.write(f"The selected number is {slider_value}")

# Add a text input
user_input = st.text_input("Enter some text")

# Display the user input
if user_input:
    st.write(f"You entered: {user_input}")

# Display a data table
data = pd.DataFrame({
    'Numbers': np.arange(1, 11),
    'Squares': np.arange(1, 11) ** 2
})

st.write("Here is a sample data table:")
st.table(data)

# Display a line chart
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['A', 'B', 'C']
)

st.line_chart(chart_data)