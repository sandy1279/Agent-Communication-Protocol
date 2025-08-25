

ACP-based Multi-Agent Orchestration 🚀

This repository demonstrates how to use Agent Communication Protocol (ACP) for reliable, scalable, and structured multi-agent communication.

Unlike Agent-to-Agent (A2A) messaging—where agents directly call each other (leading to tight coupling, brittle flows, and poor scalability)—ACP introduces a client–server communication layer that ensures loose coupling and robust orchestration.


---

🔧 How It Works

ACP Client → Orchestrates workflows, maintains context, and communicates requests/responses.

ACP Server (Agents) → Implements agent logic and exposes tools in a structured way.

Protocol Layer → Provides standardized message passing, session handling, and orchestration.


This separation of concerns ensures decoupled agents, easier debugging, and reliable workflows.


---

🚀 Getting Started

1. Start the Agent Servers

python AgentServer1.py
python AgentServer2.py

2. Run the Orchestrator (ACP Client)

python Orchestrator.py


---

🔍 Why ACP over A2A?

Feature	A2A (Agent-to-Agent)	ACP (Agent Communication Protocol)

Coupling	High (agents depend directly)	Low (decoupled via client/server)
Scalability	Limited	High – agents can be added/removed independently
Context Handling	Manual, error-prone	Built-in session + context handling
Debugging	Hard (messages scattered)	Centralized orchestration in ACP client
Reliability	Lower (fragile links)	Higher (structured protocol + fallbacks)



---

✅ Benefits

Loose coupling → Agents evolve independently

Structured orchestration → Centralized client manages flows

Session management → Context-aware workflows

Scalable design → Plug-and-play agents