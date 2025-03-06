import os
import pytest
from unittest.mock import patch
from promptrefiner.config import load_config


def test_load_config_with_explicit_values():
    """Test load_config when all parameters are explicitly provided."""
    result = load_config(api_key="test_key", model="custom_model", temperature=0.7)
    assert result == {
        "api_key": "test_key",
        "model": "custom_model",
        "temperature": 0.7,
    }


@patch.dict(
    os.environ,
    {
        "PREFINER_API_KEY": "env_key",
        "PREFINER_MODEL": "env_model",
        "PREFINER_TEMP": "0.5",
    },
)
def test_load_config_with_env_variables():
    """Test load_config when values are taken from environment variables."""
    result = load_config()
    assert result == {
        "api_key": "env_key",
        "model": "env_model",
        "temperature": 0.5,
    }


@patch.dict(os.environ, {}, clear=True)
def test_load_config_with_defaults():
    """Test load_config when no parameters or environment variables are provided."""
    result = load_config()
    assert result == {
        "api_key": None,  # No API key provided
        "model": "openai/gpt-3.5-turbo",  # Default model
        "temperature": 0.0,  # Default temperature
    }


@patch.dict(os.environ, {"PREFINER_API_KEY": "env_key"})
def test_load_config_with_partial_env():
    """Test load_config when some values are provided via environment variables."""
    result = load_config(model="custom_model")
    assert result == {
        "api_key": "env_key",  # Taken from environment
        "model": "custom_model",  # Explicitly provided
        "temperature": 0.0,  # Default value
    }


@patch.dict(os.environ, {"PREFINER_TEMP": "1.2"})
def test_load_config_with_partial_env_and_arguments():
    """Test load_config when mixing explicit arguments and environment variables."""
    result = load_config(api_key="explicit_key")
    assert result == {
        "api_key": "explicit_key",  # Explicitly provided
        "model": "openai/gpt-3.5-turbo",  # Default model
        "temperature": 1.2,  # Taken from environment
    }


def test_load_config_with_invalid_temperature():
    """Test load_config when PREFINER_TEMP is set to a non-float value."""
    with patch.dict(os.environ, {"PREFINER_TEMP": "invalid"}):
        with pytest.raises(
            ValueError, match="could not convert string to float: 'invalid'"
        ):
            load_config()
