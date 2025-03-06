import pytest
from unittest.mock import MagicMock, patch
from promptrefiner.base import BaseStrategy


class DummyStrategy(BaseStrategy):
    """Concrete implementation of BaseStrategy for testing."""

    def get_system_prompt(self):
        return "System prompt for strategy."


@patch("promptrefiner.base.load_config")
@patch("promptrefiner.base.get_llm_client")
def test_base_strategy_initialization_with_defaults(
    mock_get_llm_client, mock_load_config
):
    """Test BaseStrategy initialization when no explicit llm_client is provided."""
    mock_load_config.return_value = {
        "api_key": "test_key",
        "model": "test_model",
        "temperature": 0.7,
    }
    mock_get_llm_client.return_value = MagicMock()

    strategy = DummyStrategy()

    mock_load_config.assert_called_once_with(None, None, None)
    mock_get_llm_client.assert_called_once_with("test_key", "test_model", None)
    assert strategy.llm_client == mock_get_llm_client.return_value


def test_base_strategy_initialization_with_llm_client():
    """Test BaseStrategy when llm_client is explicitly provided."""
    mock_client = MagicMock()
    strategy = DummyStrategy(llm_client=mock_client)

    assert strategy.llm_client == mock_client


@patch("promptrefiner.base.get_llm_client")
def test_base_strategy_initialization_with_explicit_params(mock_get_llm_client):
    """Test BaseStrategy when API key, model, and temperature are passed explicitly."""
    mock_get_llm_client.return_value = MagicMock()

    strategy = DummyStrategy(
        api_key="custom_key", model="custom_model", temperature=0.9
    )

    mock_get_llm_client.assert_called_once_with("custom_key", "custom_model", 0.9)
    assert strategy.llm_client == mock_get_llm_client.return_value


def test_base_strategy_refine():
    """Test that refine calls llm_client with correct system prompt and user prompt."""
    mock_client = MagicMock()
    strategy = DummyStrategy(llm_client=mock_client)

    strategy.refine("Test prompt")

    mock_client.assert_called_once_with("System prompt for strategy.", "Test prompt")


def test_base_strategy_cannot_be_instantiated():
    """Test that BaseStrategy cannot be instantiated directly (enforces abstract methods)."""
    with pytest.raises(
        TypeError, match="Can't instantiate abstract class BaseStrategy"
    ):
        BaseStrategy()
