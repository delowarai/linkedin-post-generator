# AI-Powered LinkedIn Post Generator

Built with LangChain and GitHub Models API.

## Agent Workflow

```
User Input (Topic + Language)
         |
         v
 [ Router Agent ]  <- LangChain Chain: Classifies topic as TECH or GENERAL
         |
    _____|_____
    |         |
  TECH      GENERAL
    |         |
    v         v
 Tech      General
 Writer    Writer
 Agent     Agent
 (LangChain)(LangChain)
    |         |
    |_________|
         |
         v
  Final LinkedIn Post
```

## Tech Stack

- LangChain — Agent framework and chain building
- LangChain OpenAI — LLM integration
- GitHub Models API — AI model provider
- python-dotenv — Environment variable management

## Files

| File | Description |
|------|-------------|
| v1_basic_agent.py | Basic LangChain LLM call |
| v2_router_agent.py | LangChain chain that classifies topic as Tech or General |
| v3_writer_agents.py | Tech Writer and General Writer agents using LangChain |
| v4_linkedin_generator.py | Final version with full conditional routing logic |

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

## LangChain Usage

Each agent uses a LangChain chain built with the pipe operator:

```python
chain = prompt | llm
response = chain.invoke({"topic": topic, "language": language})
```

## Routing Logic

```python
classification = router_agent(topic)

if classification["category"] == "tech":
    post = tech_writer_agent(topic, language)
else:
    post = general_writer_agent(topic, language)
```

## Examples

- Example 1: AI in Healthcare -> TECH -> Tech Writer Agent -> English post
- Example 2: Remote Work Productivity -> GENERAL -> General Writer Agent -> Bangla post