import os
import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from agent import research_agent # Ensure agent.py is in the same folder

app = FastAPI(title="Research Agent API")

# Enable CORS so your local HTML file can talk to this server
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://hamzaahmedkhan786.github.io/"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ResearchRequest(BaseModel):
    topic: str
    provider: str  # "openai", "groq", or "ollama"
    api_key: str
    tavily_key: str

@app.post("/run-research")
async def run_research(request: ResearchRequest):
    # Set the Tavily key for searching
    os.environ["TAVILY_API_KEY"] = request.tavily_key
    
    # Set the LLM key (unless using Ollama)
    if request.provider == "openai":
        os.environ["OPENAI_API_KEY"] = request.api_key
    elif request.provider == "groq":
        os.environ["GROQ_API_KEY"] = request.api_key

    try:
        initial_state = {
            "topic": request.topic,
            "provider": request.provider,
            "context": [],
            "queries": []
        }
        
        # Run the agent
        result = research_agent.invoke(initial_state)
        return {"status": "success", "report": result.get("report")}
        
    except Exception as e:
        print(f"Error: {e}")
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        # Security: Remove keys from memory after the task finishes
        for key in ["OPENAI_API_KEY", "GROQ_API_KEY", "TAVILY_API_KEY"]:
            os.environ.pop(key, None)

if __name__ == "__main__":
    # Use the port assigned by Render, default to 8000 for local testing
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)