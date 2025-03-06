"""
PromptRefiner: A Python package for enhancing and refining prompts for LLM applications.
"""

import logging
from .refiner import PromptRefiner

logging.getLogger(__name__).addHandler(logging.NullHandler())

__version__ = "0.1.0"

__all__ = ["PromptRefiner"]
