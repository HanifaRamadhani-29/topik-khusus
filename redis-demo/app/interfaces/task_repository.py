from abc import ABC, abstractmethod
from app.domain.task import Task

class TaskRepository(ABC):
    @abstractmethod
    def save(self, task: Task) -> Task:
        raise NotImplementedError

    @abstractmethod
    def get(self, task_id: str) -> Task | None:
        raise NotImplementedError
