from tasks.task_models import Task, create_task


class TaskFactory:
    """Factory for creating new tasks using configured task types."""

    def __init__(self, allowed_task_types: list[str]) -> None:
        self.allowed_task_types = allowed_task_types

    def create(self, task_type: str, payload: dict) -> Task:
        """Create and validate a task before enqueueing."""
        return create_task(task_type, payload, self.allowed_task_types)
