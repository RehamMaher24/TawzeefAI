"""Single entry point that coordinates TawzeefAI agents."""

from typing import Any

from app.agents.router import TaskRouter


class AgentOrchestrator:
    """Routes a task to its responsible agent workflow.

    Keep cross-agent coordination here; individual workflows belong in their
    respective domain modules rather than in API route handlers.
    """

    def __init__(self, router: TaskRouter | None = None) -> None:
        self.router = router or TaskRouter()

    async def execute(self, task_type: str, payload: dict[str, Any]) -> Any:
        handler = self.router.resolve(task_type)
        return await handler(payload)
