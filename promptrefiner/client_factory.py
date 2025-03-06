"""
Implements `get_llm_client` method to configure `litellm.completion`
to communicate with user provided LLM client.
"""

import os
import litellm
from typing import Callable

# Mapping of models to their required API key environment variable
# to provide abstraction to library users.
MODEL_API_KEY_MAP = {
    "openai": "OPENAI_API_KEY",
    "anthropic": "ANTHROPIC_API_KEY",
    "togethercomputer": "TOGETHER_API_KEY",
    "ai21": "AI21_API_KEY",
    "nlpcloud": "NLP_CLOUD_API_KEY",
    "xai": "XAI_API_KEY",
    "nvidia_nim": "NVIDIA_NIM_API_KEY",
    "huggingface": "HUGGINGFACE_API_KEY",
    "azure": "AZURE_API_KEY",
    "openrouter": "OPENROUTER_API_KEY",
    "jina_ai": "JINA_AI_API_KEY",
    "mistral": "MISTRAL_API_KEY",
    "gemini": "GEMINI_API_KEY",
    "databricks": "DATABRICKS_API_KEY",
    "watsonx": "WATSONX_APIKEY",
    "cerebras": "CEREBRAS_API_KEY",
    "volcengine": "VOLCENGINE_API_KEY",
    "perplexity": "PERPLEXITYAI_API_KEY",
    "friendliai": "FRIENDLI_TOKEN",
    "galadriel": "GALADRIEL_API_KEY",
    "topaz": "TOPAZ_API_KEY",
    "groq": "GROQ_API_KEY",
    "github": "GITHUB_API_KEY",
    "deepseek": "DEEPSEEK_API_KEY",
    "fireworks_ai": "FIREWORKS_AI_API_KEY",
    "clarifai": "CLARIFAI_API_KEY",
    "cloudflare": "CLOUDFLARE_API_KEY",
    "deepinfra": "DEEPINFRA_API_KEY",
    "voyage": "VOYAGE_API_KEY",
    "baseten": "BASETEN_API_KEY",
    "sambanova": "SAMBANOVA_API_KEY",
}


def get_llm_client(api_key: str, model: str, temperature: float, **kwargs) -> Callable:
    """
    Generate a lambda function around ` litellm.completion` to be called
    from `PromptRefiner.refine`.

    Args:
        api_key (str): API key to access model.
        model (str): model name to use for refining prompt.
        temperature (float): Temperature for model.
        **kwargs: Extra arguments to feed into model.

    Returns:
        A lambda function, which takes `system_prompt` and `user_prompt`
            as an argument and retunrs refined prompt on call.
    """

    # Identify which environment variable `litellm` expects for the chosen model
    provider = model.split("/")[0]
    expected_env_var = MODEL_API_KEY_MAP.get(provider)

    # Set the API key dynamically for the expected environment variable
    if expected_env_var and api_key:
        os.environ[expected_env_var] = api_key

    # Return a function that calls litellm
    return lambda system_prompt, user_prompt: litellm.completion(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        temperature=temperature,
        **kwargs,
    )["choices"][0]["message"]["content"]
