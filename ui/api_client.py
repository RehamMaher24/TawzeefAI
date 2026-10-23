"""Small client boundary between Streamlit and the backend API."""

import os

import httpx


class TawzeefAPIClient:
    def __init__(self, base_url: str | None = None) -> None:
        self.base_url = base_url or os.getenv("API_BASE_URL", "http://localhost:8000")

    def health(self) -> dict:
        response = httpx.get(f"{self.base_url}/api/v1/health", timeout=10)
        response.raise_for_status()
        return response.json()
