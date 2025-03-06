from abc import ABC, abstractmethod
from .client_factory import get_llm_client
from promptrefiner.config import load_config


class BaseStrategy(ABC):
    """Abstract base class for all prompt refinement strategies."""

    def __init__(
        self,
        llm_client=None,
        api_key=None,
        model=None,
        temperature=None,
        **kwargs,
    ):
        """
        Initializes with OpenAI API credentials (defaults to global config).
        """
        if llm_client:
            self.llm_client = llm_client
        else:
            config = load_config(api_key, model, temperature)
            self.llm_client = get_llm_client(
                config["api_key"], config["model"], temperature, **kwargs
            )

    @abstractmethod
    def get_system_prompt(self) -> str:  # pragma: no cover
        """Each strategy must define its own system prompt."""
        pass

    def refine(self, prompt: str) -> str:
        """Refine a prompt using OpenAI API, applying strategy-specific system instructions."""
        return self.llm_client(self.get_system_prompt(), prompt)
