"""Schemas shared by multiple API domains."""

from pydantic import BaseModel


class HealthResponse(BaseModel):
    status: str
