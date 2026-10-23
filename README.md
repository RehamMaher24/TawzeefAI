# TawzeefAI

An AI-powered recruitment platform with a modular FastAPI backend and Streamlit user interface.

## Quick start

1. Create a virtual environment and install the project: `pip install -e .[dev]`
2. Copy `.env.example` to `.env` and adjust settings as needed.
3. Start the backend: `uvicorn app.main:app --reload`
4. In a second terminal, start the UI: `streamlit run ui/streamlit_app.py`

The health endpoint is available at `http://localhost:8000/api/v1/health`.
