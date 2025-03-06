# Contributing to PromptRefiner

Thank you for your interest in contributing to **PromptRefiner**! 🚀 This guide will help you set up a development environment and contribute effectively.

---

## 🛠 Setting Up the Development Environment

### 1️⃣ **Clone the Repository**
```sh
git clone https://github.com/darshit7/promptrefiner.git
cd promptrefiner
```

### 2️⃣ **Install Hatch (if not installed)**
We use **Hatch** for dependency management and virtual environments. If you don’t have it installed, run:
```sh
pip install hatch
```

### 3️⃣ **Create and Activate the Development Environment**
To set up your environment, run:
```sh
hatch env create dev
hatch shell dev
```
This installs all dependencies listed under `[tool.hatch.envs.dev]` in `pyproject.toml`.

### 4️⃣ **Verify Installation**
To confirm everything is set up correctly, run:
```sh
pytest  # Runs tests
mypy .  # Runs type checks
ruff check .  # Runs linter
```

---

## 🏗 Making Contributions

### **🐛 Found a Bug?**
- Open an issue describing the bug and steps to reproduce.
- If you already have a fix, feel free to submit a PR!

### **✨ Adding a Feature?**
- Discuss your idea in an issue first.
- Follow best practices for writing clean, maintainable Python code.

### **📝 Writing Documentation?**
- We use **MkDocs** with `mkdocs-material`. Run `mkdocs serve` locally to preview changes.

---

## 🔄 Running Tests
Before submitting a PR, ensure all tests pass:
```sh
pytest
```

If adding new functionality, include appropriate tests.

---

## 🚀 Submitting a Pull Request
1. **Fork the repository** and create a new branch.
2. Make your changes and commit them with a meaningful message.
3. Push your branch and open a PR.
4. Ensure your PR follows the style guide and passes all checks.

---

## 🛡 Code Style & Linting
We enforce **PEP8** and other best practices using `ruff`, `black`, and `mypy`. Before committing, format your code:
```sh
black .
ruff check . --fix
mypy .
```

---

## 🙌 Join the Community
We welcome contributions of all kinds! Whether it's code, documentation, or discussions, your input is valuable.

Feel free to **open an issue** or **join discussions** to help improve PromptRefiner! 🚀
