import streamlit as st

def set_bg_video():
    video_url = "https://cdn.pixabay.com/video/2023/03/23/155788-811409230_large.mp4"

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
        /* Box styles */
        .container {{
            background-color: rgba(0, 0, 0, 0.8); /* Semi-transparent black */
            border-radius: 20px; /* Rounded corners */
            padding: 40px; /* Padding around the content */
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2); /* Shadow for depth */
            width: 80%; /* Adjust width as needed */
            margin: auto; /* Center the box */
            text-align: center; /* Center align text inside the box */
        }}
        /* Title styles */
        .title {{
            font-family: serif;  /* Use default serif font */
            color: #f2b807;  /* Title color */
            font-size: 100px; /* Increased font size for the title */
            margin: 0;  /* Remove default margin */
        }}
        /* Button styles */
        .get-started-button {{
            background-color: #B9FF66; /* Light blue button background color */
            color: black; /* Button text color */
            font-size: 32px; /* Increased button font size */
            padding: 10px 35px; /* Increased button padding */
            border: none; /* Remove border */
            border-radius: 10px; /* More rounded corners */
            cursor: pointer; /* Pointer cursor */
            transition: background-color 0.5s; /* Slower transition effect */
            margin-top: 20px; /* Margin above the button */
            text-decoration: none; /* Remove underline from link */
        }}
        /* Ensure the link remains black and non-underlined on hover */
        .get-started-button:hover {{
            background-color: #B9FF66; /* Button hover color */
            color: black; /* Keep text color black on hover */
            text-decoration: none; /* Ensure no underline on hover */
        }}
        .get-started-button:visited {{
            color: black; /* Ensure visited link color is black */
        }}
        </style>
        <video class="video-bg" autoplay loop muted>
            <source src="{video_url}" type="video/mp4">
            Your browser does not support the video tag.
        </video>
        """,
        unsafe_allow_html=True
    )

# Set page configuration
st.set_page_config(
    page_title="CareerQuest",
    page_icon="🏆",  # You can choose any emoji or icon
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Set the background video
set_bg_video()

# Create a container with rounded corners and semi-transparency
st.markdown("""
    <div class="container">
        <div class="title">CareerQuest</div>
        <a href="https://careerquest1.streamlit.app/._Career_Path" class="get-started-button">GET STARTED</a>
    </div>
""", unsafe_allow_html=True)
