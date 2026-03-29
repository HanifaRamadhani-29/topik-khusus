import logging
from typing import Dict

from queue.task_queue import TaskQueue
from tasks.task_factory import TaskFactory
from tasks.task_models import Task

logger = logging.getLogger(__name__)


class TaskProducer:
    """Producer responsible for submitting tasks into the queue."""

    def __init__(self, task_queue: TaskQueue, task_factory: TaskFactory) -> None:
        self._task_queue = task_queue
        self._task_factory = task_factory

    def submit_task(self, task_type: str, payload: Dict[str, object]) -> Task:
        """Validate and enqueue a new task."""
        task = self._task_factory.create(task_type, payload)
        self._task_queue.enqueue(task)
        logger.info("Task submitted: %s", task.task_id)
        return task
