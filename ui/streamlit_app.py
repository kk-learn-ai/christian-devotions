import streamlit as st
import os
import sys

# Add the project root directory to the Python path
project_root = os.path.abspath(os.path.dirname(__file__))
sys.path.append(project_root)

from utils.api_key_utils import validate_openai_api_key

def show_openai_instructions():
    """
    Display instructions for obtaining an OpenAI API key using Streamlit components.

    This function creates an expandable section in the Streamlit app that provides
    step-by-step instructions on how to obtain an OpenAI API key. It includes both
    a brief overview and detailed instructions that can be revealed with a button click.

    The function uses Streamlit's expander and markdown components to structure
    and display the information in a user-friendly format.

    Note:
        This function does not return any value. It directly renders content
        to the Streamlit app interface.

    Example:
        >>> show_openai_instructions()
        # This will display an expander in the Streamlit app with API key instructions
    """
    
    with st.expander("How to Get Your OpenAI API Key", expanded=False):
        st.markdown("""
        ## 🔑 Getting Your OpenAI API Key

        Follow these steps to obtain your OpenAI API key:

        1. Visit [OpenAI's website](https://platform.openai.com/)
        2. Sign up or log in to your account
        3. Navigate to API keys in your account settings
        4. Create a new API key
        5. Copy and securely store your API key
        6. Set up billing in your account
        7. Set usage limits (optional)

        For detailed instructions, click the button below.
        """)
        
        if st.button("View Detailed Instructions"):
            st.markdown("""
            ### Detailed Instructions:

            1. **Visit OpenAI's website**: Go to [https://platform.openai.com/](https://platform.openai.com/)
            2. **Sign up or log in**: 
               - New users: Click "Sign up" and create an account
               - Existing users: Click "Log in"
            3. **Navigate to API keys**: 
               - Look for your account name/icon in the top-right corner
               - Click to open the dropdown menu
               - Select "View API keys"
            4. **Create a new API key**: 
               - Look for "Create new secret key" or "+ New secret key"
               - Optionally, give your key a name
            5. **Copy and save your API key**: 
               - The key will be displayed only once
               - Copy it immediately and store it securely
            6. **Set up billing**: 
               - Find the "Billing" or "Payment" section in account settings
               - Add a payment method
            7. **Set usage limits (optional)**: 
               - In the billing section, you may be able to set spending limits

            Remember to keep your API key confidential and never share it publicly.
            """)

def main():
    st.title('Christian Devotions Project')
    st.write('Welcome to the Christian Devotions Project!')

    st.markdown("""
    This project implements a modular system for publishing Christian daily devotions using the crewAI library. The system is designed to streamline the process of creating, editing, and managing inspirational content to encourage readers in their faith journey.
    """)
    
    st.markdown("---")  # This adds a horizontal line for separation

    st.markdown("""
    To start, you need to key in your OpenAI API key.
    """)

    show_openai_instructions()  # give an option for pop-up for obtaining OpenAI API key instruction

    # Check if API key is already stored in session state
    if 'openai_api_key' not in st.session_state:
        st.session_state.openai_api_key = ''

    # API key input
    api_key = st.text_input('Enter your OpenAI API Key:', 
                            type='password', 
                            value=st.session_state.openai_api_key)

    if api_key:
        if validate_openai_api_key(api_key):
            st.session_state.openai_api_key = api_key
            st.success('OpenAI API Key is valid and stored for this session!')
            
            # Here you can add more Streamlit components to interact with your project
            theme = st.text_input("Enter the theme for the devotional series:")
            if theme:
                st.write(f"You entered: {theme}")
                # Here you would typically call your devotional creation functions
                # For example: create_devotional_series(theme, st.session_state.openai_api_key)
        else:
            st.error(f'Invalid API key: {api_key[:5]}...{api_key[-5:]}')
            st.error('Please check your API key and try again.')
    else:
        st.warning('Please enter your OpenAI API Key to proceed.')

    # Add a note about session-based storage
    st.info('Note: Your API key is stored only for the duration of this session and will need to be re-entered if you close the app.')

if __name__ == '__main__':
    main()
