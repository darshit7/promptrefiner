import pytest
import openai
from click.testing import CliRunner
from unittest.mock import patch

from promptrefiner.cli import main
from promptrefiner.strategies import STRATEGY_MAP


@pytest.fixture
def runner():
    return CliRunner()


def test_help_message(runner):
    """Test if help message displays correctly"""
    result = runner.invoke(main, ["--help"])
    assert result.exit_code == 0
    assert "Usage:" in result.output
    assert "Available Strategies" in result.output


def test_missing_strategy(runner):
    """Test CLI when no strategy is provided"""
    result = runner.invoke(main, ["This is a test prompt"])
    assert result.exit_code != 0
    assert "Missing option '--strategy'" in result.output


def test_invalid_strategy(runner):
    """Test CLI when an invalid strategy is passed"""
    result = runner.invoke(main, ["Test prompt", "-s", "x"])
    assert result.exit_code != 0
    assert "Error: Unknown strategy 'x'" in result.output


@patch("promptrefiner.cli.PromptRefiner")
def test_valid_strategy(mock_refiner, runner):
    """Test CLI when a valid strategy is used"""
    mock_instance = mock_refiner.return_value
    mock_instance.refine.return_value = "Refined prompt output"

    strategy_name = next(iter(STRATEGY_MAP.keys()))  # Get any valid strategy
    result = runner.invoke(main, ["Test prompt", "-s", strategy_name])

    assert result.exit_code == 0
    assert "Strategies Applied:" in result.output
    assert "Refined Prompt:" in result.output
    assert "Refined prompt output" in result.output


@patch("promptrefiner.cli.PromptRefiner")
def test_openai_error_handling(mock_refiner, runner):
    """Test handling of OpenAI API errors"""
    mock_refiner.side_effect = Exception("Mocked OpenAI error")

    strategy_name = next(iter(STRATEGY_MAP.keys()))
    result = runner.invoke(main, ["Test prompt", "-s", strategy_name])

    assert result.exit_code == 1


@patch(
    "promptrefiner.cli.PromptRefiner.refine",
    side_effect=openai.OpenAIError("API Error"),
)
def test_openai_api_error_handling(mock_refine, runner):
    """Test handling of OpenAI API errors"""
    strategy_name = next(iter(STRATEGY_MAP.keys()))  # Get any valid strategy
    result = runner.invoke(main, ["Test prompt", "-s", strategy_name])

    assert result.exit_code == 1
    assert "API Error" in result.output
