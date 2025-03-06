# Promptrefiner
## 🚀 Welcome to Promptrefiner

> **Helping you craft the perfect prompt for better LLM responses!**

PromptRefiner is a lightweight **Python library** that helps users **write better prompts** for Large Language Models (LLMs) with minimal configurations. Many users struggle to craft effective prompts that yield the desired results.  

PromptRefiner **takes user input**, applies a **selected strategy**, and **returns an improved prompt** to get **more specific and effective responses from LLMs (Large Language Models).** It achieves this by leveraging an **LLM to refine the user’s prompt** based on predefined strategies, making it easier to get high-quality responses.

Whether you're using a prompt for **GPT-4, Claude, Mistral, or any other LLM**, PromptRefiner ensures **your input is well-structured** for the best possible output.

---

## ✨ Key Features

✅ **Supports 100+ LLM Clients** – Works with OpenAI, Anthropic, Hugging Face, and more!  
✅ **Highly Customizable** – Use different LLM clients per strategy or a single client for all.  
✅ **Command-Line First** – Quickly refine prompts from the CLI for rapid experimentation.  
✅ **Extensible** – Developers can create their own **custom prompt refinement strategies**.  
✅ **Seamless Integration** – Works effortlessly in Python applications or scripts.  

---

## 📥 Installation

Install PromptRefiner using pip:

```sh
pip install promptrefiner
```

---

## ⚡ Quick Start

### 🔧 **Using from the Command Line**

Before using `promptrefiner` in Python, make sure to **set environment variables** (Windows users should use set instead of export):  

```sh
export PREFINER_API_KEY="your-api-key-here"
export PREFINER_MODEL="openai/gpt-4"  # Change based on your LLM model
```

and there you go...  

```sh
promptrefiner --strategy persona "Tell me about AI"
```

### 🐍 **Using in a Python Script**

!!! note
    Make sure to **set environment variables** `PREFINER_API_KEY` and `PREFINER_MODEL` before using `PromptRefiner` in your python script.

```python
from promptrefiner import PromptRefiner

prompt_refiner = PromptRefiner(strategies=["persona"])
refined_prompt = prompt_refiner.refine("Explain quantum mechanics.")
print(refined_prompt)
```

---

## 🔍 How It Works

1. **User provides a prompt** (e.g., "Tell me about AI").
2. **Selects a strategy** (e.g., "verbose" for a more detailed response).
3. **PromptRefiner applies a system prompt template** for that strategy.
4. **Sends it to an LLM** for refinement.
5. **Returns the improved prompt** back to the user.

🚀 **Under the hood:** Each strategy is backed by a system prompt template that guides the LLM to refine the user’s input for better results.

---

## 🤔 Why Use PromptRefiner?

🔹 **Improve prompt clarity & effectiveness** – Get sharper, more relevant responses.  
🔹 **Save time** – No need to manually tweak prompts for better results.  
🔹 **Optimized for developers & researchers** – Quickly test different prompting strategies.  
🔹 **Fine-tune for different LLMs** – Customize strategies for specific AI models.  
🔹 **Works for various use cases:**  

- Chatbots & AI assistants
- Content generation & summarization
- Data extraction from LLMs
- Code generation improvements

---

## 🚀 Join Us & Contribute!

We welcome **contributors, feedback, and feature suggestions!** 🚀

📌 **GitHub Repo**: [darshit7/promptrefiner](https://github.com/darshit7/promptrefiner)  
📌 **Documentation**: [Promptrefiner](https://darshit7.github.io/promptrefiner/)  
📌 **Report Issues & Ideas**: [Coming Soon](#)

👥 **Want to improve PromptRefiner?** Open a GitHub issue or contribute a pull request! 🛠️

---

🚀 **Refine your prompts. Supercharge your AI interactions. Try PromptRefiner today!**