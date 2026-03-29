import threading
from collections import deque
from typing import Deque, Optional

from tasks.task_models import Task


class TaskQueue:
    """A thread-safe FIFO queue for task dispatching."""

    def __init__(self, max_size: int = 100) -> None:
        self._max_size = max_size
        self._tasks: Deque[Task] = deque()
        self._lock = threading.Lock()

    def enqueue(self, task: Task) -> None:
        """Add a new task to the queue, raising if capacity is reached."""
        with self._lock:
            if len(self._tasks) >= self._max_size:
                raise OverflowError("Task queue is full")
            self._tasks.append(task)

    def dequeue(self) -> Optional[Task]:
        """Remove the oldest task from the queue, or return None if empty."""
        with self._lock:
            return self._tasks.popleft() if self._tasks else None

    def requeue(self, task: Task) -> None:
        """Place a task back at the end of the queue for retry."""
        with self._lock:
            if len(self._tasks) >= self._max_size:
                raise OverflowError("Task queue is full")
            self._tasks.append(task)

    def size(self) -> int:
        """Return the current number of tasks waiting in the queue."""
        with self._lock:
            return len(self._tasks)

    def is_empty(self) -> bool:
        """Return True when the queue has no waiting tasks."""
        return self.size() == 0
