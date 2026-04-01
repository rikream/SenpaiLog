# AI Research Assistant Bot

An AI-powered research assistant built using LangChain and Groq LLM APIs.  
This project generates structured research outputs using prompt templates, tool-calling agents, and Pydantic output parsing.

---

## Features

- AI research query assistant  
- Structured JSON output parsing  
- Wikipedia and web search integration  
- Automatic research result saving to text file  
- Environment-based API key handling  

---

## Tech Stack

- Python  
- LangChain  
- Groq LLM API  
- Pydantic  
- DuckDuckGo Search  
- Wikipedia API  

---

## Setup Instructions

### 1. Clone repository

```bash
git clone https://github.com/yourusername/ai-bot.git
cd ai-bot
```

### 2. Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add environment variable

Create a `.env` file:

```
GROQ_API_KEY=your_api_key_here
```

---

## Run Project

```bash
python main.py
```

Then enter your research query when prompted.

---

## Project Structure

```
AI BOT/
│── main.py
│── tools.py
│── research_output.txt
│── requirements.txt
│── README.md
│── .env (ignored)
```

---

## Important Notes

- Do NOT upload `.env` file to GitHub.  
- Add `.env` to `.gitignore`.

Example `.gitignore`:

```
.env
__pycache__/
venv/
aiml_project_env/
```

---

## Author

Rikim Rana
