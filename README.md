# Agent-Communication-Protocol
an implementation of ACP given by IBM using its sdk 

# ACP Agents with CrewAI + TinyLlama

This project demonstrates how to build autonomous agents using [ACP](https://github.com/agenta-ai/acp), 
[CrewAI](https://github.com/joaomdmoura/crewai), 
and the TinyLlama 1.1B Chat model running locally via [Ollama](https://ollama.ai).  

The system is split into three components:
1. **ACP Client** – Handles the connection to ACP servers and orchestrates workflows between agents.
2. **Research Drafter Agent (ACP Server)** – Generates initial research summaries.
3. **Research Verifier Agent (ACP Server)** – Fact-checks and enhances summaries using web search tools.

---

## 📂 Project Structure

.
├── acp_client.py # ACP client (workflow orchestration + connection)
├── AgentServer1.py # ACP server: drafts research summaries
├── AgentServer2.py # ACP server: fact-checks & enhances summaries
└── README.md


---

## ⚙️ Requirements

- Python 3.10+
- [Ollama](https://ollama.ai) installed and running
- Models pulled locally:

Install dependencies:

pip install acp-sdk crewai smolagents duckduckgo-search
🚀 Usage
1. Start the ACP Servers (Agents)
Run the research Agent file:

Run the research verifier:

Both agents will run as independent ACP servers (listening on different ports, e.g., 8000 and 8001).
