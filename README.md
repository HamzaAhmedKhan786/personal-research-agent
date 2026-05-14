# 🔍 Personal Research Agent (PRA)

An autonomous AI research assistant built with **LangGraph**, **FastAPI**, and **Tavily**. This agent doesn't just answer questions—it plans, researches, critiques, and iterates until the job is done.

## 🚀 Key Features
- **Agentic Workflow**: Uses a stateful graph to handle research loops and self-correction.
- **Deep Research**: Powered by the Tavily AI search engine for high-signal data retrieval.
- **Human-in-the-Loop**: Optional checkpoints to approve research plans before final report generation.
- **Secure BYOK Model**: Users provide their own OpenAI and Tavily API keys; keys are never stored on the server.
- **Auto-Iterate**: If the initial results are insufficient, the agent automatically refines its search queries.

## 🛠️ Tech Stack
- **Orchestration**: LangGraph (Stateful Directed Acyclic Graphs)
- **Brain**: OpenAI GPT-4o / Claude 3.5 Sonnet
- **Search**: Tavily API (AI-native search)
- **Backend**: FastAPI (Python)
- **Frontend**: HTML5/Tailwind CSS (Hosted on GitHub Pages)

## 📁 Repository Structure
```text
.
├── backend/
│   ├── main.py          # FastAPI entry point
│   ├── agent.py         # LangGraph logic (Nodes & Edges)
│   └── requirements.txt
├── frontend/
│   └── index.html       # UI for API key input and research results
├── .github/workflows/
│   └── deploy.yml       # Auto-deploy frontend to GitHub Pages
└── README.md
