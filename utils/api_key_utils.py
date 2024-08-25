# utils/api_key_utils.py

from openai import OpenAI, AuthenticationError

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
    except Exception:
        return False


