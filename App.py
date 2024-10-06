import streamlit as st

def main():
    # Set up the home page layout
    st.title("Career Quest")
    st.subheader("Welcome to Career Quest")
    st.write("Your journey towards a successful career starts here!")

    # Button to navigate to the Uni-Finder page
    if st.button("Get Started"):
        # Navigate to the Uni-finder page
        st.experimental_set_query_params(page="Uni-finder")
        st.experimental_rerun()

if __name__ == "__main__":
    main()
