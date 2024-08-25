# utils/api_key_utils.py

import os
import getpass
from typing import Optional
from openai import OpenAI, AuthenticationError, OpenAIError

def get_openai_api_key() -> str:
    """
    Prompts the user for their OpenAI API key securely and validates it.
    Returns the key if valid, None otherwise.
    """
    while True:
        api_key = getpass.getpass('Please enter your OpenAI API key: ')
        if validate_openai_api_key(api_key):
            return api_key
        else:
            print(f'Invalid API key: {api_key[:5]}...{api_key[-5:]}')
            print('Please check your API key and try again.')

def validate_openai_api_key(api_key: str) -> bool:
    """
    Validates the OpenAI API key by attempting to create a client.
    Returns True if valid, False otherwise.
    """
    try:
        client = OpenAI(api_key=api_key)
        # Attempt a simple API call to validate the key
        client.models.list()
        return True
    except AuthenticationError:
        return False
    except OpenAIError as e:
        print(f'An error occurred while validating the API key: {e}')
        return False

def load_openai_api_key() -> Optional[str]:
    """
    Retrieves the OpenAI API key from an environment variable.
    If not found or invalid, prompts the user to enter it.
    """
    api_key = os.getenv('OPENAI_API_KEY')
    if api_key and validate_openai_api_key(api_key):
        return api_key
    else:
        return get_openai_api_key()
