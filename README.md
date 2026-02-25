# CodeMap CLI

![CodeMap Preview](https://raw.githubusercontent.com/purvaspatel/codemap/main/assets/image.png)

AI-ready project structure generator for developers.

CodeMap generates a clean, IDE-style tree of your project so you can easily share your codebase structure with AI tools like ChatGPT or Claude.

---

## Why CodeMap?

When working with AI tools, developers often need to explain their entire project structure before asking meaningful questions.

Manually typing folder trees is slow and error-prone.

CodeMap solves this by generating a clean, deterministic structure of your repository in seconds.

---

## Features

- Automatic project root detection  
- Python and JavaScript ecosystem detection  
- Smart ignore rules  
- Collapses large directories (e.g., `node_modules`)  
- Hides environment and cache files  
- Detects structural changes and updates output  
- Colored CLI feedback  
- Generates `codemap.md`  

---

## Installation

```bash
pip install codemap-cli