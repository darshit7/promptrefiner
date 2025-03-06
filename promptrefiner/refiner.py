"""
This module defines the main `PromptRefiner` class and associated functions
for modifying and enhancing prompts using various strategies.
"""

import logging
from promptrefiner.base import BaseStrategy
from promptrefiner.strategies import STRATEGY_MAP

logger = logging.getLogger(__name__)


class PromptRefiner(object):
    """
    A class for refining prompt using multiple strategies.

    This class applies a series of transformations to enhance a given input prompt.
    It supports multiple strategies, such as "few_shot" and "meta".

    Attributes:
        strategies (list[str|BaseStrategy]): A list of strategies to be applied
            to the prompt.
    """

    def __init__(self, strategies: list):
        """
        Initialize the `PromptRefiner` with list of strategies.

        Args:
            strategies (list): A list of supported strategies.

        Raises:
            ValueError: If provided strategy is not supported.
        """
        if not strategies:
            raise ValueError("At least one strategy must be provided.")

        self.strategies = []
        for strategy in strategies:
            if isinstance(strategy, str):
                normalized_name = next(
                    (
                        name
                        for name, data in STRATEGY_MAP.items()
                        if strategy.lower() in [name] + data["aliases"]
                    ),
                    None,
                )
                if not normalized_name:
                    raise ValueError(f"Unsupported strategy: {strategy}")
                strategy_class = STRATEGY_MAP[normalized_name]["class_"]
                self.strategies.append(strategy_class())
            elif isinstance(strategy, type) and issubclass(strategy, BaseStrategy):
                self.strategies.append(strategy())  # Instantiate class
            elif isinstance(strategy, BaseStrategy):
                self.strategies.append(strategy)  # Already instantiated
            else:
                logger.error(f"Invalid strategy: {strategy}")
                raise ValueError(f"Invalid strategy: {strategy}")
        logger.info(f"PromptRefiner initialized with strategies: {self.strategies}")

    def refine(self, prompt: str) -> str:
        """
        Applies all strategies in sequence and returns refined prompt.

        Args:
            prompt (str): The input prompt.

        Returns:
            str: The refined prompt after applying strategies.
        """
        for strategy in self.strategies:
            prompt = strategy.refine(prompt)
        return prompt
