"""Registry-based routing for agent tasks and paths."""

from collections.abc import Awaitable, Callable
from typing import Any

AgentHandler = Callable[[dict[str, Any]], Awaitable[Any]]


class TaskRouter:
    """Maps task names such as ``candidate_screening`` to agent handlers."""

    def __init__(self) -> None:
        self._handlers: dict[str, AgentHandler] = {}

    def register(self, task_type: str, handler: AgentHandler) -> None:
        self._handlers[task_type] = handler

    def resolve(self, task_type: str) -> AgentHandler:
        try:
            return self._handlers[task_type]
        except KeyError as exc:
            raise ValueError(f"No agent workflow registered for '{task_type}'.") from exc
