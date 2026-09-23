<div align="center">

#  AI-Powered LinkedIn Post Generator

### Multi-Agent Content Automation System built with LangChain & LLMs

*An intelligent AI agent that reads a topic, decides its category, and writes a publish-ready LinkedIn post - automatically.*

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![LangChain](https://img.shields.io/badge/LangChain-Agent%20Framework-1C3C3C?style=for-the-badge&logo=chainlink&logoColor=white)](https://www.langchain.com/)
[![OpenAI](https://img.shields.io/badge/LLM-GPT--4.1--nano-412991?style=for-the-badge&logo=openai&logoColor=white)](https://platform.openai.com/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](#license)

[Overview](#-overview) • [How It Works](#-how-it-works) • [Features](#-features) • [Tech Stack](#-tech-stack) • [Quick Start](#-quick-start) • [Demo](#-demo) • [Roadmap](#-roadmap) • [Contact](#-lets-connect)

</div>

---

## 📌 Overview

Manually writing engaging, on-brand LinkedIn content every day doesn't scale. This project solves that with a **multi-agent AI pipeline** — instead of a single prompt-to-output call, it uses **conditional agent routing** to decide *how* a post should be written before it's written, resulting in more relevant, higher-quality content every time.

Give it a **topic** and a **language**, and the system:

1. Classifies the topic (Tech vs. General)
2. Routes it to a specialized writer agent trained for that voice
3. Returns a publish-ready post — formatted, on-tone, and CTA-driven

This project demonstrates practical, production-style **agentic AI architecture** — the same pattern used in real-world content, support, and workflow-automation tools.

---

## How It Works

```
                     ┌────────────────────────────┐
                     │   User Input (Topic + Lang) │
                     └──────────────┬─────────────┘
                                    │
                                    ▼
                     ┌────────────────────────────┐
                     │     Agent 1 — Router        │
                     │  Classifies topic as        │
                     │     TECH or GENERAL         │
                     └──────────────┬─────────────┘
                                    │
                     ┌──────────────┴──────────────┐
                     ▼                              ▼
        ┌─────────────────────┐        ┌─────────────────────┐
        │   Agent 2            │        │   Agent 3            │
        │   Tech Writer         │        │   General Writer      │
        │   Professional,       │        │   Warm, mentor-like,  │
        │   industry-aware      │        │   relatable            │
        └──────────┬───────────┘        └──────────┬───────────┘
                     │                              │
                     └──────────────┬───────────────┘
                                    ▼
                     ┌────────────────────────────┐
                     │     Final LinkedIn Post      │
                     └────────────────────────────┘
```

This is a classic **conditional routing** pattern — the same architecture used in real enterprise AI agents that triage and dispatch tasks to specialized sub-agents.

---

## Features

- 🤖 **Multi-Agent Architecture** — Router + specialized writer agents, not a single generic prompt
- 🌐 **Multi-Language Support** — Generates posts in any language the user specifies (including Bangla)
- 🎯 **Smart Topic Classification** — Automatically detects Tech vs. General content and adapts tone
- ✍️ **Publish-Ready Output** — 2–4 paragraphs, natural emoji use, and a closing question/CTA for engagement
- 💾 **Auto-Save to File** — Exports generated posts to a UTF-8 text file for easy reuse
- 🔌 **Pluggable LLM Backend** — Powered by GitHub Models API, easily swappable with any OpenAI-compatible provider
- 🧩 **Clean, Incremental Codebase** — Versioned build (`v1` → `v4`) showing clear architectural progression from a basic LLM call to a full routed agent system

---

## Tech Stack

| Layer | Technology |
|---|---|
| Agent Framework | [LangChain](https://www.langchain.com/) |
| LLM Integration | LangChain OpenAI |
| Model Provider | GitHub Models API (`openai/gpt-4.1-nano`) |
| Config Management | `python-dotenv` |
| Language | Python 3.10+ |

---

## Project Structure

| File | Description |
|---|---|
| `v1_basic_agent.py` | Baseline LangChain LLM call |
| `v2_router_agent.py` | **Agent 1** — Classifies topic as Tech or General |
| `v3_writer_agents.py` | **Agent 2 & 3** — Tech Writer and General Writer agents |
| `v4_linkedin_generator.py` | Final version — full conditional routing pipeline |
| `save_output.py` | Saves generated post to `linkedin_output.txt` (UTF-8) |
| `requirements.txt` | Project dependencies |

---

## Quick Start

### 1. Clone the repository
```bash
git clone https://github.com/delowarhossaincse63/linkedin-post-generator.git
cd linkedin-post-generator
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure environment variables
Create a `.env` file in the project root:
```env
BASE_URL=https://models.github.ai/inference/v1
API_KEY=your-github-token-here
MODEL_NAME=openai/gpt-4.1-nano
```

### 4. Run the generator
```bash
python v4_linkedin_generator.py
```

### 5. (Optional) Save output to file
```bash
python save_output.py
```

---

## Demo

**Example 1 — Tech Topic (English)**
```
Topic    : AI in Healthcare
Language : English
Category : TECH → routed to Tech Writer Agent
```

**Example 2 — General Topic (Bangla)**
```
Topic    : Remote Work Productivity
Language : Bangla
Category : GENERAL → routed to General Writer Agent
```

---

## Roadmap

- [ ] Streamlit / web UI for non-technical users
- [ ] Direct LinkedIn API publishing integration
- [ ] Post scheduling & content calendar
- [ ] Hashtag & image suggestion agent
- [ ] Analytics agent (predict engagement before posting)

---

## Let's Connect

I build practical, production-style **AI agents and LLM-powered automation systems** — from multi-agent pipelines like this one to full-stack AI integrations for businesses.

If you're looking to automate content, workflows, or customer interactions with AI, I'd love to talk.

📧 **Email:** your-email@example.com
💼 **LinkedIn:** [linkedin.com/in/your-profile](https://linkedin.com)
🐙 **GitHub:** [@delowarhossaincse63](https://github.com/delowarhossaincse63)

---

## License

This project is licensed under the [MIT License](LICENSE).

<div align="center">

If you find this project useful, consider giving it a star — it helps a lot!

</div>
