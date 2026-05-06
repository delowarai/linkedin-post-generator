# AI-Powered LinkedIn Post Generator

An AI Agent built with LangChain that generates professional LinkedIn posts based on user-provided topic and language.

---

## Agent Workflow

```
User Input (Topic + Language)
         |
         v
 [ Agent 1: Router Agent ]
 Analyzes and classifies topic
 as TECH or GENERAL
         |
    _____|_____
    |         |
  TECH      GENERAL
    |         |
    v         v
[ Agent 2 ]  [ Agent 3 ]
Tech Writer  General Writer
  Agent        Agent
    |         |
    |_________|
         |
         v
  Final LinkedIn Post
```

---

## Agents

### Agent 1 — Router Agent
- File: `v2_router_agent.py`
- Job: Reads the topic and classifies it as `tech` or `general`
- Uses: LangChain `ChatPromptTemplate` + `ChatOpenAI`
- Output: `{"category": "tech", "reason": "..."}`

### Agent 2 — Tech Writer Agent
- File: `v3_writer_agents.py`
- Triggered when: Router classifies topic as `tech`
- Style: Professional, insightful, industry-aware
- Output: 2-4 paragraphs, ends with question or CTA

### Agent 3 — General Writer Agent
- File: `v3_writer_agents.py`
- Triggered when: Router classifies topic as `general`
- Style: Warm, mentor-like, relatable
- Output: 2-4 paragraphs, ends with question or CTA

---

## Conditional Routing Logic

```python
classification = router_agent(topic)

if classification["category"] == "tech":
    post = tech_writer_agent(topic, language)   # Agent 2
else:
    post = general_writer_agent(topic, language) # Agent 3
```

---

## Post Requirements

- 2 to 4 short paragraphs
- Professional and engaging tone
- Ends with a question or call-to-action
- Written in the user-selected language
- 1 to 3 emojis

---

## Tech Stack

- LangChain — Agent framework and chain building
- LangChain OpenAI — LLM integration
- GitHub Models API — AI model provider (openai/gpt-4.1-nano)
- python-dotenv — Environment variable management

---

## Project Files

| File | Description |
|------|-------------|
| `v1_basic_agent.py` | Basic LangChain LLM call |
| `v2_router_agent.py` | Agent 1 — Classifies topic as Tech or General |
| `v3_writer_agents.py` | Agent 2 and 3 — Tech Writer and General Writer |
| `v4_linkedin_generator.py` | Final version with full conditional routing |
| `save_output.py` | Saves output to linkedin_output.txt with UTF-8 encoding |
| `requirements.txt` | Python dependencies |
| `README.md` | Project documentation |

---

## Setup

### 1. Install dependencies
```
pip install -r requirements.txt
```

### 2. Create .env file
```
BASE_URL=https://models.github.ai/inference/v1
API_KEY=your-github-token-here
MODEL_NAME=openai/gpt-4.1-nano
```

### 3. Run
```
python v4_linkedin_generator.py
```

### 4. Save output to file
```
python save_output.py
```

---

## Demo Examples

### Example 1 — Tech Topic (English)
```
Topic    : AI in Healthcare
Language : English
Category : TECH
Writer   : Tech Writer Agent
```

### Example 2 — General Topic (Bangla)
```
Topic    : Remote Work Productivity
Language : Bangla
Category : GENERAL
Writer   : General Writer Agent
```