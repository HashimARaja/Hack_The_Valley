import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import google.generativeai as genai
import graphviz  # Import graphviz for visualization
import os


# Configure the API key for Generative AI
genai.configure(api_key=st.secrets["API_KEY"])


# Set the title of the app with a background color
st.markdown(
   """
   <style>
   .main {
       background-color: #f0f2f5;
   }
   .title {
       color: #2b2d42;
       font-size: 32px;
   }
   .subheader {
       color: #8d99ae;
   }
   </style>
   """,
   unsafe_allow_html=True
)


# Set the title and subtitle
st.title("🎓 University Program Finder")
st.subheader("Discover Educational Paths Tailored for You")


# Add a text input for user queries
user_input_1 = st.text_input("Enter your country")
user_input_2 = st.text_input("Enter your field of study")


# Display the user input if provided
if user_input_1 and user_input_2:  # Check both user inputs
   st.success(f"You entered: **Country:** {user_input_1}, **Field of Study:** {user_input_2}")


   # Set the variables x and p from user inputs
   x = user_input_2  # Field of study
   p = user_input_1  # Country


   # Call the Generative AI model
   model = genai.GenerativeModel(model_name="gemini-1.5-flash")
   response = model.generate_content(
       "for the following career path: " + x +
       "\nProvide a concise Education path and goals for this career path and include a variety of " +
       p + " University programs to choose from and beginning, middle and end stage jobs (Provide Links next to where you see fit)"
   )



