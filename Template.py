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


# Introduction text
st.write("""
This interactive web application helps you explore various educational programs and scholarships tailored to marginalized communities.
Use the sidebar to input your preferences and discover suitable options.
""")


# Create a sidebar for user inputs
st.sidebar.title("Input Menu")
st.sidebar.write("Use the options below to interact with the app.")


# Add a slider to the sidebar for selecting a number
slider_value = st.sidebar.slider("Select a number (0-100)", 0, 100, 50)
st.sidebar.write(f"You selected: **{slider_value}**")


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
       p + " University programs to choose from and beginning, middle and end stage jobs"
   )


   # Display the response from the model
   st.write("### Suggested Educational Path and Job Options:")
   st.write(response.text)


   # Create a colorful flowchart using Graphviz
   dot = graphviz.Digraph()


   # Add colorful nodes
   dot.node('A', f'Field of Study: {x}', style='filled', fillcolor='lightblue', fontcolor='black')
   dot.node('B', f'Programs in {p}', style='filled', fillcolor='blue', fontcolor='black')
   dot.node('C', 'Beginner Job', style='filled', fillcolor='yellow', fontcolor='black')
   dot.node('D', 'Mid-Level Job', style='filled', fillcolor='orange', fontcolor='black')
   dot.node('E', 'Senior Job', style='filled', fillcolor='lightcoral', fontcolor='black')


   # Connect the nodes with colorful edges
   dot.edge('A', 'B', 'Choose Programs', color='blue')
   dot.edge('B', 'C', 'Entry-Level Positions', color='green')
   dot.edge('C', 'D', 'Gain Experience', color='orange')
   dot.edge('D', 'E', 'Advance Career', color='red')


   # Render the flowchart
   st.graphviz_chart(dot)


# Generate sample data for visuals
data = pd.DataFrame({
   'Program': ['Medicine', 'Engineering', 'Arts', 'Science', 'Business'],
   'Scholarships': np.random.randint(5, 20, size=5)
})


# Display the bar chart for scholarships available
st.write("### Scholarships Available by Program:")
fig, ax = plt.subplots()
sns.barplot(x='Program', y='Scholarships', data=data, palette='pastel', ax=ax)
ax.set_title('Number of Scholarships by Program', fontsize=16)
ax.set_ylabel('Number of Scholarships', fontsize=12)
ax.set_xlabel('Programs', fontsize=12)
st.pyplot(fig)


# Create a sample data table
data_table = pd.DataFrame({
   'Numbers': np.arange(1, 11),
   'Squares': np.arange(1, 11) ** 2
})


# Display the data table with enhanced formatting
st.write("### Sample Data Table:")
st.table(data_table.style.highlight_max(axis=0))


# Generate random data for a line chart with Seaborn
chart_data = pd.DataFrame(
   np.random.randn(20, 3),
   columns=['Category A', 'Category B', 'Category C']
)


# Set the style for seaborn
sns.set(style='whitegrid')


# Create a line chart
st.write("### Random Data Line Chart:")
fig, ax = plt.subplots()
sns.lineplot(data=chart_data, palette='tab10', ax=ax)
ax.set_title('Random Data Trends', fontsize=16)
ax.set_ylabel('Values', fontsize=12)
ax.set_xlabel('Index', fontsize=12)
st.pyplot(fig)


# Optional: Additional features or information
st.write("""
### Additional Features
Explore more options to refine your search and get tailored recommendations based on your input.
""")

