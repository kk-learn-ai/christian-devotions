import streamlit as st
import os
import sys

# Add the project root directory to the Python path
project_root = os.path.abspath(os.path.dirname(__file__))
sys.path.append(project_root)

from utils.api_key_utils import validate_openai_api_key

def main():
    st.title('Christian Devotions Project')
    st.write('Welcome to the Christian Devotions Project!')

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
