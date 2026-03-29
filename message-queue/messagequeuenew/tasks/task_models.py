import uuid
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from enum import Enum
from typing import Any, Dict


class TaskStatus(str, Enum):
    """Task lifecycle states."""

    PENDING = "pending"
    PROCESSING = "processing"
    COMPLETED = "completed"
    FAILED = "failed"


@dataclass
class Task:
    """Represents a unit of work in the task processing system."""

    task_id: str
    task_type: str
    payload: Dict[str, Any]
    status: TaskStatus = TaskStatus.PENDING
    attempts: int = 0
    error_message: str = ""
    created_at: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    updated_at: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())

    def mark_processing(self) -> None:
        self.status = TaskStatus.PROCESSING
        self.updated_at = datetime.utcnow().isoformat() + "Z"

    def mark_completed(self) -> None:
        self.status = TaskStatus.COMPLETED
        self.updated_at = datetime.utcnow().isoformat() + "Z"

    def mark_failed(self, message: str) -> None:
        self.status = TaskStatus.FAILED
        self.error_message = message
        self.updated_at = datetime.utcnow().isoformat() + "Z"

    def increment_attempts(self) -> None:
        self.attempts += 1
        self.updated_at = datetime.utcnow().isoformat() + "Z"

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


def create_task(task_type: str, payload: Dict[str, Any], allowed_types: list[str]) -> Task:
    """Create a validated Task instance from raw input."""
    if task_type not in allowed_types:
        raise ValueError(f"Invalid task type: {task_type}")
    if not isinstance(payload, dict):
        raise ValueError("Task payload must be a dictionary")
    if not payload:
        raise ValueError("Task payload cannot be empty")

    return Task(task_id=str(uuid.uuid4()), task_type=task_type, payload=payload)
