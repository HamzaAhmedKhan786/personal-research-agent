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
```
---
## 🌍 How to Run the App (No Coding Required)

You can run the research agent directly from your browser via the GitHub Pages link. Depending on your preference, you can use a "Cloud Brain" or a "Local Brain".

### 1. Access the Live Site
Visit the hosted link: `https://your-username.github.io/personal-research-agent/`.

### 2. Choose Your "Brain" (AI Model)
The app offers three ways to power the research:

#### **Option A: Groq (Recommended - Free & Fast)**
* **Cost**: Free.
* **Step**: Get a free API key from the [Groq Console](https://console.groq.com/).
* **Usage**: Select **Groq** in the app, paste your key, and start researching.

#### **Option B: OpenAI (Paid)**
* **Cost**: Requires a paid API balance or trial.
* **Step**: Generate a key at the [OpenAI Platform](https://platform.openai.com/).

#### **Option C: Ollama (100% Private & Local)**
If you want the AI to run on your own computer, you can link your local Ollama instance to the GitHub Pages site.

1.  **Install Ollama**: Download and install it from [ollama.com](https://ollama.com).
2.  **Run a Model**: Open your terminal and run `ollama run llama3.1`.
3.  **Bridge to GitHub Pages**: To allow the website to talk to your computer, you must restart Ollama with permission for your site. Close Ollama and run the following command:
    * **Windows (PowerShell)**: 
        ```powershell
        $env:OLLAMA_ORIGINS="[https://your-username.github.io](https://your-username.github.io)"; ollama serve
        ```
    * **Mac/Linux**: 
        ```bash
        OLLAMA_ORIGINS="[https://your-username.github.io](https://your-username.github.io)" ollama serve
        ```
4.  **Use the App**: Select **Ollama** in the browser. No API key is needed for the LLM.

### 3. Get Your "Eyes" (Tavily Search Key)
Regardless of the brain you choose, the agent needs to search the web.
* **Step**: Sign up at [Tavily.com](https://tavily.com/) for a free search API key.

---

## 📄 Professional Exports
Once the research is complete, you can save your findings in two professional formats:
* **PDF**: Generates a clean, formal document with standardized margins and clear headings. All web UI elements like buttons and input boxes are automatically hidden.
* **Word (.docx)**: Downloads a true Word file that you can open and edit in Microsoft Word for final adjustments.

---

## 🛡️ Privacy & Security
* **Local Storage**: All files you "Save" are downloaded directly to your computer and are never stored on a server.
* **Secure Keys**: Your API keys are used only for the current session and are never saved or shared.