import os
import sys
from typing import Optional

# Add the project root directory to the Python path
project_root = os.path.abspath(os.path.dirname(__file__))
sys.path.append(project_root)

from utils.api_key_utils import get_openai_api_key, load_openai_api_key, validate_openai_api_key

def main() -> None:
    """
    Main function to run the application.
    """
    api_key: Optional[str] = load_openai_api_key()
    if api_key is not None:
        print('OpenAI API Key has been set for this session.')
    else:
        print('Failed to obtain a valid OpenAI API key.')

if __name__ == '__main__':
    main()
