import logging
from typing import Any

from queue.task_queue import TaskQueue
from tasks.task_handlers import execute_task
from tasks.task_models import Task

logger = logging.getLogger(__name__)


class TaskConsumer:
    """Consumer that processes tasks from the queue asynchronously."""

    def __init__(self, task_queue: TaskQueue, retry_limit: int) -> None:
        self._task_queue = task_queue
        self._retry_limit = retry_limit

    def process_next(self) -> Any:
        """Process the next pending task from the queue."""
        task = self._task_queue.dequeue()
        if task is None:
            logger.debug("No task available to process")
            return None

        task.increment_attempts()
        task.mark_processing()
        logger.info("Processing task %s of type %s", task.task_id, task.task_type)

        try:
            result = execute_task(task)
            task.mark_completed()
            logger.info("Task %s completed: %s", task.task_id, result)
            return result
        except Exception as error:
            task.mark_failed(str(error))
            logger.warning(
                "Task %s failed on attempt %d: %s",
                task.task_id,
                task.attempts,
                task.error_message,
            )
            if task.attempts <= self._retry_limit:
                logger.info("Retrying task %s (%d/%d)", task.task_id, task.attempts, self._retry_limit)
                self._task_queue.requeue(task)
            return None

    def process_all(self, max_iterations: int = 100) -> None:
        """Process tasks until the queue is empty or the iteration limit is reached."""
        processed = 0
        while processed < max_iterations and not self._task_queue.is_empty():
            self.process_next()
            processed += 1
