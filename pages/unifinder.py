import streamlit as st
import google.generativeai as genai

# Function to set background video
def set_bg_video():
    video_url = "https://media.istockphoto.com/id/2154818320/video/hyperlapse-aerial-view-smart-city-wireless-network-signal-data-transmission-high-speed-and.mp4?s=mp4-640x640-is&k=20&c=wmi66ui27aEtxpULSttCsneb1Lmry_9sRYs3i3ZB7_o="

    st.markdown(
        f"""
        <style>
        .video-bg {{
            position: fixed;
            top: 0;
            left: 0;
            min-width: 100%;
            min-height: 100%;
            z-index: -1;
            overflow: hidden;
        }}
        .stApp {{
            background-color: rgba(0, 0, 0, 0.7); /* Dark overlay for better text visibility */
        }}
        /* Customize title and subtitle fonts and colors */
        .title {{
            font-family: serif;  /* Use default serif font */
            color: #FFFFFF;  /* Set title color to white */
            font-size: 32px;
            font-weight: bold;  /* Make the title bold */
            text-align: center;  /* Center align the title */
            margin-bottom: 10px;  /* Add margin below the title */
        }}
        .subtitle {{
            font-family: serif;  /* Use default serif font */
            color: #FFFFFF;  /* Set subtitle color to white */
            font-size: 24px;  /* Adjust font size */
            font-weight: 300;  /* Lighter font weight for a softer look */
            text-align: center;  /* Center align the subtitle */
            padding-bottom: 20px;  /* Add padding below the subtitle */
        }}
        /* Change the text input box styles */
        .stTextInput label {{
            color: #FFFFFF;  /* Set label color to white */
        }}
        .stTextInput input {{
            background-color: #FFFFFF;  /* White background for input fields */
            color: #000000;  /* Set input text color to black */
            border: 1px solid #CCCCCC;  /* Light grey border for the input box */
            border-radius: 5px;  /* Rounded corners */
            padding: 10px;  /* Padding inside the input field */
        }}
        /* Set the color for all text outputs */
        .stMarkdown, .stSuccess, .stWrite {{
            color: #FFFFFF;  /* Set the color of markdown, success, and other text outputs to white */
        }}
        </style>
        <video class="video-bg" autoplay loop muted>
            <source src="{video_url}" type="video/mp4">
            Your browser does not support the video tag.
        </video>
        """,
        unsafe_allow_html=True
    )

# Configure the API key for Generative AI
genai.configure(api_key=st.secrets["API_KEY"])

# Call the function to set the background video
set_bg_video()

# Set the title and subtitle with custom HTML for color and size
st.markdown("<h1 class='title'>University Program Finder</h1>", unsafe_allow_html=True)
st.markdown("<h2 class='subtitle'>Discover Educational Paths Tailored for You</h2>", unsafe_allow_html=True)

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
        p + " University programs to choose from and beginning, middle and end stage jobs (Provide Links for the Universities)"
    )

    # Display the response from the model
    st.write("### Suggested Educational Path and Job Options:")
    st.write(response.text)
