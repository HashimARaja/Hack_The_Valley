import streamlit as st
import pandas as pd
import re

# Set page configuration
st.set_page_config(
    page_title="Scholarship Finder",
    page_icon="🎓",
    layout="wide",
)

st.title("🎓 Scholarship Finder")
st.write("Find scholarships that match your criteria.")

# Load the CSV file into a DataFrame
scholarships_df = pd.read_csv('scholarships.csv')

# Sidebar filters inside a form
with st.sidebar.form(key='filter_form'):
    
    st.header("Filter Scholarships")
    
    # Race filter (Text input)
    race_input = st.text_input(
        "Race/Ethnicity",
        placeholder="e.g., African American, Asian"
    )
    
    # Gender filter (Text input)
    gender_input = st.text_input(
        "Gender",
        placeholder="e.g., Female, Male"
    )
    
    # Sexuality filter (Text input)
    sexuality_input = st.text_input(
        "Sexuality",
        placeholder="e.g., LGBTQ+, Heterosexual"
    )
    
    # Field of Study filter (Text input)
    field_of_study = st.text_input(
        "Field of Study",
        placeholder="e.g., Engineering, Medicine"
    )
    
    # Household Income filter (Text input)
    income_input = st.text_input(
        "Household Income",
        placeholder="e.g., Below $30,000"
    )
    
    # Keyword search input
    keywords_input = st.text_input(
        "Keywords (separate with commas)",
        placeholder="e.g., leadership, community service"
    )
    
    # Apply Filters button
    submit_button = st.form_submit_button(label='Apply Filters')

if submit_button:
    # Process keywords
    keywords = [word.strip() for word in keywords_input.split(',') if word.strip() != '']
    
    # Copy the original DataFrame
    filtered_df = scholarships_df.copy()
    
    # Apply Race filter
    if race_input and 'Race' in filtered_df.columns:
        filtered_df = filtered_df[filtered_df['Race'].str.contains(race_input, case=False, na=False)]
    
    # Apply Gender filter
    if gender_input and 'Gender' in filtered_df.columns:
        filtered_df = filtered_df[filtered_df['Gender'].str.contains(gender_input, case=False, na=False)]
    
    # Apply Sexuality filter
    if sexuality_input and 'Sexuality' in filtered_df.columns:
        filtered_df = filtered_df[filtered_df['Sexuality'].str.contains(sexuality_input, case=False, na=False)]
    
    # Apply Household Income filter
    if income_input and 'Household Income' in filtered_df.columns:
        filtered_df = filtered_df[filtered_df['Household Income'].str.contains(income_input, case=False, na=False)]
    
    # Apply Field of Study filter
    if field_of_study:
        filtered_df = filtered_df[
            filtered_df['Description'].str.contains(field_of_study, case=False, na=False) | 
            filtered_df['Scholarship Name'].str.contains(field_of_study, case=False, na=False)
        ]
    
    # Combine all text columns for keyword search
    if keywords:
        filtered_df['combined_text'] = filtered_df.apply(lambda row: ' '.join(map(str, row.values)), axis=1)
        pattern = '|'.join(re.escape(keyword) for keyword in keywords)
        filtered_df = filtered_df[filtered_df['combined_text'].str.contains(pattern, case=False, na=False)]
        filtered_df = filtered_df.drop(columns=['combined_text'])
    
    # Store the filtered DataFrame in session state
    st.session_state.filtered_df = filtered_df

    # Reset scholarship_index for pagination
    st.session_state.scholarship_index = 0

# Check if filtered_df is in session state
if 'filtered_df' in st.session_state:
    filtered_df = st.session_state.filtered_df
    st.subheader("Available Scholarships")
    
    if not filtered_df.empty:
        # Reset index for better display
        filtered_df.reset_index(drop=True, inplace=True)
        
        # Display total scholarships found
        total_scholarships = len(filtered_df)
        st.write(f"Total scholarships found: {total_scholarships}")
        
        # Number of scholarships to display per page
        SCHOLARSHIPS_PER_PAGE = 10
        # Calculate the subset of scholarships to display
        start_idx = st.session_state.scholarship_index
        end_idx = start_idx + SCHOLARSHIPS_PER_PAGE
        scholarships_to_display = filtered_df.iloc[start_idx:end_idx]
        
        # Display scholarships
        for idx, row in scholarships_to_display.iterrows():
            st.markdown(f"### {row['Scholarship Name']}")
            st.write(f"**Amount:** ${row['Amount']}")
            st.write(f"**Deadline:** {row['Deadline']}")
            st.write(f"**Description:** {row['Description']}")
            st.write(f"**Location:** {row['Location']}")
            st.write(f"**Years:** {row['Years']}")
            st.write(f"[More Information]({row['Link']})")
            st.markdown("---")
        
        # Navigation buttons
        col1, col2, col3 = st.columns([1, 2, 1])
        with col1:
            if st.button("Previous"):
                if st.session_state.scholarship_index >= SCHOLARSHIPS_PER_PAGE:
                    st.session_state.scholarship_index -= SCHOLARSHIPS_PER_PAGE
        with col2:
            page_number = (st.session_state.scholarship_index // SCHOLARSHIPS_PER_PAGE) + 1
            total_pages = ((total_scholarships - 1) // SCHOLARSHIPS_PER_PAGE) + 1
            st.write(f"Page {page_number} of {total_pages}")
        with col3:
            if st.button("Next"):
                if st.session_state.scholarship_index + SCHOLARSHIPS_PER_PAGE < total_scholarships:
                    st.session_state.scholarship_index += SCHOLARSHIPS_PER_PAGE
    else:
        st.write("No scholarships match your criteria.")
else:
    st.write("Use the filters on the sidebar and click 'Apply Filters' to see scholarships that match your criteria.")
