import os
from typing import List


class Settings:
    """Application settings loaded from environment variables."""

    def __init__(self) -> None:
        self.queue_max_size = int(os.getenv("TASK_QUEUE_MAX_SIZE", "100"))
        self.retry_limit = int(os.getenv("TASK_RETRY_LIMIT", "3"))
        self.log_level = os.getenv("LOG_LEVEL", "INFO").upper()
        self.allowed_task_types = [
            "resize_image",
            "calculate_sum",
            "convert_file",
        ]
        self.worker_batch_size = int(os.getenv("WORKER_BATCH_SIZE", "5"))

    def validate(self) -> None:
        if self.queue_max_size < 1:
            raise ValueError("TASK_QUEUE_MAX_SIZE must be at least 1")
        if self.retry_limit < 0:
            raise ValueError("TASK_RETRY_LIMIT must be zero or positive")
        if self.worker_batch_size < 1:
            raise ValueError("WORKER_BATCH_SIZE must be at least 1")
