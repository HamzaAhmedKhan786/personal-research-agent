import os
from typing import TypedDict, List
from langgraph.graph import StateGraph, END
from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
from langchain_ollama import ChatOllama
from tavily import TavilyClient

# 1. Define the shared data structure
class AgentState(TypedDict):
    topic: str
    provider: str
    queries: List[str]
    context: List[str]
    report: str
    iteration: int

# 2. Brain Factory: Selects the model based on user choice
def get_model(state: AgentState):
    provider = state.get("provider", "openai")
    if provider == "openai":
        return ChatOpenAI(model="gpt-4o-mini", temperature=0.2)
    elif provider == "groq":
        # Llama 3.3 70B is currently the best free model on Groq
        return ChatGroq(model="llama-3.3-70b-versatile", temperature=0.2)
    elif provider == "ollama":
        # Requires 'ollama run llama3.1' to be running locally
        return ChatOllama(model="llama3.1")

# 3. Node: Planning search queries
def planner(state: AgentState):
    llm = get_model(state)
    prompt = f"Target Topic: {state['topic']}. Generate 3 targeted search queries to gather comprehensive data. Return only the queries, one per line."
    response = llm.invoke(prompt)
    queries = [q.strip("- ").strip("123456789. ") for q in response.content.split("\n") if q.strip()]
    return {"queries": queries}

# 4. Node: Executing web searches
def search(state: AgentState):
    tavily = TavilyClient(api_key=os.environ["TAVILY_API_KEY"])
    search_context = []
    for query in state["queries"]:
        results = tavily.search(query=query, search_depth="advanced")
        for res in results['results']:
            search_context.append(f"Source: {res['url']}\nContent: {res['content']}")
    return {"context": search_context}

# 5. Node: Synthesizing the final report
def synthesizer(state: AgentState):
    llm = get_model(state)
    context_text = "\n\n".join(state["context"])
    prompt = f"Topic: {state['topic']}\n\nUsing this data:\n{context_text}\n\nWrite a professional research report."
    response = llm.invoke(prompt)
    return {"report": response.content}

# 6. Build the Graph
workflow = StateGraph(AgentState)
workflow.add_node("planner", planner)
workflow.add_node("search", search)
workflow.add_node("synthesizer", synthesizer)

workflow.set_entry_point("planner")
workflow.add_edge("planner", "search")
workflow.add_edge("search", "synthesizer")
workflow.add_edge("synthesizer", END)

research_agent = workflow.compile()