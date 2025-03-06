import os
import pytest
from unittest.mock import patch
from promptrefiner.client_factory import get_llm_client, MODEL_API_KEY_MAP


@pytest.fixture
def mock_litellm():
    """Mock litellm.completion response."""
    with patch("promptrefiner.client_factory.litellm.completion") as mock:
        mock.return_value = {"choices": [{"message": {"content": "Refined prompt"}}]}
        yield mock


def test_get_llm_client_sets_env_variable(mock_litellm):
    """Test that get_llm_client sets the correct environment variable for API key."""
    model = "openai/gpt-3.5-turbo"
    api_key = "test_api_key"
    temperature = 0.7

    client = get_llm_client(api_key, model, temperature)

    expected_env_var = MODEL_API_KEY_MAP["openai"]
    assert os.environ[expected_env_var] == api_key  # Ensures env var is set

    refined_prompt = client("system message", "user message")
    assert refined_prompt == "Refined prompt"
    mock_litellm.assert_called_once()


def test_get_llm_client_with_unsupported_model(mock_litellm):
    """Test that get_llm_client does not set env var for unsupported models."""
    model = "unsupported_model/gpt-neo"
    api_key = "test_api_key"
    temperature = 0.7

    client = get_llm_client(api_key, model, temperature)

    assert "unsupported_model" not in MODEL_API_KEY_MAP  # Ensure model isn't mapped

    refined_prompt = client("system message", "user message")
    assert refined_prompt == "Refined prompt"
    mock_litellm.assert_called_once()


def test_get_llm_client_calls_litellm_correctly(mock_litellm):
    """Ensure litellm.completion is called with the correct arguments."""
    model = "openai/gpt-4"
    api_key = "test_api_key"
    temperature = 0.5

    client = get_llm_client(api_key, model, temperature)
    client("System instruction", "User input")

    mock_litellm.assert_called_once_with(
        model=model,
        messages=[
            {"role": "system", "content": "System instruction"},
            {"role": "user", "content": "User input"},
        ],
        temperature=temperature,
    )


def test_get_llm_client_handles_missing_choices(mock_litellm):
    """Test handling when litellm response has no 'choices' key."""
    mock_litellm.return_value = {}

    model = "openai/gpt-3.5-turbo"
    api_key = "test_api_key"
    temperature = 0.7

    client = get_llm_client(api_key, model, temperature)

    with pytest.raises(KeyError):
        client("system message", "user message")


def test_get_llm_client_handles_missing_message(mock_litellm):
    """Test handling when 'choices' exist but 'message' key is missing."""
    mock_litellm.return_value = {"choices": [{}]}

    model = "openai/gpt-3.5-turbo"
    api_key = "test_api_key"
    temperature = 0.7

    client = get_llm_client(api_key, model, temperature)

    with pytest.raises(KeyError):
        client("system message", "user message")


def test_get_llm_client_handles_missing_content(mock_litellm):
    """Test handling when 'message' exists but 'content' key is missing."""
    mock_litellm.return_value = {"choices": [{"message": {}}]}

    model = "openai/gpt-3.5-turbo"
    api_key = "test_api_key"
    temperature = 0.7

    client = get_llm_client(api_key, model, temperature)

    with pytest.raises(KeyError):
        client("system message", "user message")
