from app.domain.task import Task
from app.interfaces.task_repository import TaskRepository


class TaskService:
    def __init__(self, repository: TaskRepository):
        self.repository = repository

    def create_task(self, task_id: str, title: str) -> Task:
        if not task_id:
            raise ValueError("Task id is required")

        if not title or not title.strip():
            raise ValueError("Title cannot be empty")

        new_task = Task(
            id=str(task_id),
            title=title.strip(),
            completed=False
        )

        return self.repository.save(new_task)

    def get_task(self, task_id: str) -> Task | None:
        if not task_id:
            raise ValueError("Task id is required")

        return self.repository.get(task_id)