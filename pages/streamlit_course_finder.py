
import streamlit as st
import pandas as pd
import re

# Set page configuration
st.set_page_config(
    page_title="Course Finder",
    page_icon="📚",
    layout="wide",
)

st.title("📚 Course Finder")
st.write("Find courses that match your criteria.")

# Load the CSV file into a DataFrame
df = pd.read_csv('coursera-course-detail-data.csv')

# Sidebar filters inside a form
with st.sidebar.form(key='filter_form'):
    
    st.header("Filter Courses")
    
    # Difficulty filter (Text input)
    difficulty_input = st.text_input(
        "Difficulty",
        placeholder="e.g., Beginner, Intermediate, Advanced"
    )
    
    # Keyword search input
    keywords_input = st.text_input(
        "Keywords (separate with commas)",
        placeholder="e.g., Business, Software, Social Sciences"
    )
    
    # Apply Filters button
    submit_button = st.form_submit_button(label='Apply Filters')

if submit_button:
    # Process keywords
    keywords = [word.strip() for word in keywords_input.split(',') if word.strip() != '']
    
    # Copy the original DataFrame
    filtered_df = df.copy()
    
    # Apply Difficulty filter
    if difficulty_input and 'Difficulty' in filtered_df.columns:
        filtered_df = filtered_df[filtered_df['Difficulty'].str.contains(difficulty_input, case=False, na=False)]
    
    # Combine all text columns for keyword search
    if keywords:
        filtered_df['combined_text'] = filtered_df.apply(lambda row: ' '.join(map(str, row.values)), axis=1)
        pattern = '|'.join(re.escape(keyword) for keyword in keywords)
        filtered_df = filtered_df[filtered_df['combined_text'].str.contains(pattern, case=False, na=False)]
        filtered_df = filtered_df.drop(columns=['combined_text'])
    
    # Store the filtered DataFrame in session state
    st.session_state.filtered_df = filtered_df

    # Reset index for pagination
    st.session_state.course_index = 0

# Check if filtered_df is in session state
if 'filtered_df' in st.session_state:
    filtered_df = st.session_state.filtered_df
    st.subheader("Available Courses")
    
    if not filtered_df.empty:
        # Reset index for better display
        filtered_df.reset_index(drop=True, inplace=True)
        
        # Display total courses found
        total_courses = len(filtered_df)
        st.write(f"Total courses found: {total_courses}")
        
        # Number of courses to display per page
        COURSES_PER_PAGE = 10
        # Calculate the subset of courses to display
        start_idx = st.session_state.course_index
        end_idx = start_idx + COURSES_PER_PAGE
        courses_to_display = filtered_df.iloc[start_idx:end_idx]
        
        # Display courses
        for idx, row in courses_to_display.iterrows():
            st.markdown(f"### {row['Name']}")
            st.write(f"**Rating:** {row['Rating']}")
            st.write(f"**Difficulty:** {row['Difficulty']}")
            st.write(f"**Tags:** {row['Tags']}")
            st.write(f"[More Information]({row['Url']})")
            st.markdown("---")
        
        # Navigation buttons
        col1, col2, col3 = st.columns([1, 2, 1])
        with col1:
            if st.button("Previous"):
                if st.session_state.course_index >= COURSES_PER_PAGE:
                    st.session_state.course_index -= COURSES_PER_PAGE
        with col2:
            page_number = (st.session_state.course_index // COURSES_PER_PAGE) + 1
            total_pages = ((total_courses - 1) // COURSES_PER_PAGE) + 1
            st.write(f"Page {page_number} of {total_pages}")
        with col3:
            if st.button("Next"):
                if st.session_state.course_index + COURSES_PER_PAGE < total_courses:
                    st.session_state.course_index += COURSES_PER_PAGE
    else:
        st.write("No courses match your criteria.")
else:
    st.write("Use the filters on the sidebar and click 'Apply Filters' to see courses that match your criteria.")
