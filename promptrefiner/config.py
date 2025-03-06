"""
Loads configurations realted to LLM model, API keys and temprture to be used.
"""

import os


def load_config(api_key=None, model=None, temperature=None):
    """
    If `api_key`, `model` or `temperature` provided while loading config uses it,
    otherwise loads it from environment varilable.

    Args:
        api_key (str): API Key to connect with model
        model (str): model name in `litellm` supported format.
        temperature (float): temperature parameter for model.

    Returns:
        Dictionary containing `api_key`, `model` and `temperature`
    """
    api_key = api_key or os.getenv("PREFINER_API_KEY")
    model = model or os.getenv("PREFINER_MODEL", "openai/gpt-3.5-turbo")
    temperature = temperature or float(os.getenv("PREFINER_TEMP", 0))

    return {"api_key": api_key, "model": model, "temperature": temperature}
