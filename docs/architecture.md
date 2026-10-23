# TawzeefAI architecture

TawzeefAI is one modular FastAPI backend. HTTP routes stay in `app/api`, while business workflows live in their domain modules.

`app/agents` has one `AgentOrchestrator` as the entry point for AI work. Its `TaskRouter` maps each task type (for example, candidate screening or interview scheduling) to a focused agent workflow. This keeps API paths thin and lets the team add workflows independently.

The Streamlit interface in `ui/` communicates with the backend through `ui/api_client.py`.
