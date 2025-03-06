from typing import Dict, List, Type, TypedDict

from promptrefiner.base import BaseStrategy

from .persona import Persona
from .few_shot import FewShot
from .chain_of_thought import ChainofThought
from .self_consistency import SelfConsistency
from .recursive_critique_refinement import RecursiceCritiqueRefinement


class StrategyEntry(TypedDict):
    class_: Type[BaseStrategy]
    aliases: List[str]


STRATEGY_MAP: Dict[str, StrategyEntry] = {
    "persona": {"class_": Persona, "aliases": ["per"]},
    "fewshot": {"class_": FewShot, "aliases": ["fs"]},
    "chainofthought": {"class_": ChainofThought, "aliases": ["cot"]},
    "selfconsist": {"class_": SelfConsistency, "aliases": ["sc"]},
    "recref": {"class_": RecursiceCritiqueRefinement, "aliases": ["rcr"]},
}

__all__ = [
    "Persona",
    "FewShot",
    "ChainofThought",
    "SelfConsistency",
    "RecursiceCritiqueRefinement",
]
