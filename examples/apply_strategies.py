from promptrefiner import PromptRefiner
from promptrefiner.base import BaseStrategy
from promptrefiner.strategies import FewShot

# Using predefined strategy names (strings)
refiner1 = PromptRefiner(strategies=["fs"])
print(refiner1.refine("Explain quantum mechanics."))

# Directly passing strategy classes
refiner2 = PromptRefiner(strategies=[FewShot])
print(refiner2.refine("What are black holes?"))


# Mixing built-in and custom strategies
class CustomStrategy(BaseStrategy):
    def get_system_prompt(self) -> str:
        return "Custom refined strategy"


refiner3 = PromptRefiner(strategies=[CustomStrategy()])
print(refiner3.refine("Tell me about AI."))
