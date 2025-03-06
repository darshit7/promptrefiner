import pytest
from unittest.mock import MagicMock, patch
from promptrefiner.refiner import PromptRefiner
from promptrefiner.base import BaseStrategy


@pytest.fixture
def mock_strategy():
    """Fixture to create a mock strategy."""
    mock = MagicMock(spec=BaseStrategy)
    mock.refine.side_effect = lambda x: x + " refined"
    return mock


class CustomStrategy(BaseStrategy):
    """A concrete subclass of BaseStrategy for testing."""

    def get_system_prompt(self):
        return "[custom prompt]"


def test_valid_strategy(mock_strategy):
    """Test initializing PromptRefiner with valid strategies."""
    refiner = PromptRefiner([mock_strategy])
    assert len(refiner.strategies) == 1
    assert refiner.strategies[0] == mock_strategy


def test_string_strategy():
    """Test initializing PromptRefiner with a string strategy (mocked)."""
    with patch(
        "promptrefiner.refiner.STRATEGY_MAP",
        {"test": {"class_": MagicMock(spec=BaseStrategy), "aliases": ["t"]}},
    ):
        refiner = PromptRefiner(["test"])
        assert len(refiner.strategies) == 1
        assert isinstance(refiner.strategies[0], MagicMock)


def test_custom_strategy():
    """Test initializing PromptRefiner with a subclass of BaseStrategy."""
    refiner = PromptRefiner([CustomStrategy])  # Passing class, not instance
    assert len(refiner.strategies) == 1
    assert isinstance(refiner.strategies[0], CustomStrategy)


def test_invalid_strategy():
    """Test initializing PromptRefiner with an invalid strategy."""
    with pytest.raises(ValueError, match="Unsupported strategy: unknown"):
        PromptRefiner(["unknown"])


def test_with_no_strategies():
    """Test initializing PromptRefiner without any strategies."""
    with pytest.raises(ValueError, match="At least one strategy must be provided."):
        PromptRefiner([])


def test_with_invalid_type():
    """Test initializing PromptRefiner with an unsupported strategy type."""
    with pytest.raises(ValueError, match="Invalid strategy: 123"):
        PromptRefiner([123])


def test_refine(mock_strategy):
    """Test that PromptRefiner applies strategies in sequence."""
    refiner = PromptRefiner([mock_strategy, mock_strategy])
    result = refiner.refine("test prompt")
    assert result == "test prompt refined refined"
    mock_strategy.refine.assert_called()


def test_refine_with_no_modifications(mock_strategy):
    """Test when strategies return the same prompt (edge case)."""
    mock_strategy.refine.side_effect = lambda x: x  # No modification
    refiner = PromptRefiner([mock_strategy])
    result = refiner.refine("test prompt")
    assert result == "test prompt"


def test_logging_on_invalid_strategy(caplog):
    """Test if logger correctly logs an error for an invalid strategy."""
    with caplog.at_level("ERROR"):
        with pytest.raises(ValueError, match="Invalid strategy: 123"):
            PromptRefiner([123])
    assert "Invalid strategy: 123" in caplog.text
