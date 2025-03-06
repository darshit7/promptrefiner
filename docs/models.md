# 📌 Supported Models in PromptRefiner

Promptrefiner leverages **LiteLLM** under the hood, providing seamless integration with **100+ Large Language Models (LLMs)** from top AI providers like OpenAI, Anthropic, TogetherAI, AI21, and more! 🚀  

> **Why does this matter?**  
> This means **any model supported by LiteLLM** is automatically supported by Promptrefiner. You can refine your prompts using the most advanced AI models available today.

## 🎯 Supported Models
Since Promptrefiner relies on LiteLLM, it supports all models listed [here](https://docs.litellm.ai/docs/providers).

To see the full list of supported models, run:

```python
from litellm import model_list
print(model_list())
```

---

## 🎯 How Model API_KEY Selection Works?

To interact with hosted LLM you will need an API_KEY, it's confidential and mostly provided to any application from environment variable.  
When you work with **promptrefiner** you don't need to worry about it, because we internally map `PREFINER_API_KEY` to the right API key automatically!  
We've designed it to **make things easier** by allowing a single environment variable:

```bash
export PREFINER_API_KEY="your_secret_key_here"
```
!!! note
    But if you prefer provider-specific API keys, you can still use them! ✅  

## ⚡ How API Key Handling Works?
Promptrefiner automatically detects the model provider and assigns the appropriate API key.

✔ If using PREFINER_API_KEY → No extra setup needed!  
✔ If using provider-specific API keys → The library will detect and use them accordingly.  

### 🛠 Example Usage:
#### Using PREFINER_API_KEY (Recommended for Simplicity)

```bash
export PREFINER_API_KEY="your_openai_or_anthropic_key"
# If PREFINER_MODEL exported, default to openai/gpt-3.5-turbo
export PREFINER_MODEL="anthropic/claude-3.5"
```

```python
from promptrefiner import PromptRefiner

prompt_refiner = PromptRefiner(strategies=["persona"])
refined_prompt = prompt_refiner.refine("Explain quantum mechanics.")
print(refined_prompt)
```

#### Using Provider-Specific API Keys

```bash
export ANTHROPIC_API_KEY="your_anthropic_key"
# If PREFINER_MODEL exported, default to openai/gpt-3.5-turbo
export PREFINER_MODEL="anthropic/claude-3.5"
```

```python
from promptrefiner import PromptRefiner

prompt_refiner = PromptRefiner(strategies=["persona"])
refined_prompt = prompt_refiner.refine("Explain quantum mechanics.")
print(refined_prompt)
```