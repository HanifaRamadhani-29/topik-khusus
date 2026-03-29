import pytest

from queue.task_queue import TaskQueue
from tasks.task_models import Task, TaskStatus


def test_task_queue_fifo_order() -> None:
    queue = TaskQueue(max_size=3)
    task_one = Task(task_id="1", task_type="calculate_sum", payload={"values": [1]}, status=TaskStatus.PENDING)
    task_two = Task(task_id="2", task_type="convert_file", payload={"file_path": "a.txt", "target_format": "pdf"}, status=TaskStatus.PENDING)

    queue.enqueue(task_one)
    queue.enqueue(task_two)

    assert queue.dequeue() is task_one
    assert queue.dequeue() is task_two
    assert queue.dequeue() is None


def test_task_queue_enforce_max_size() -> None:
    queue = TaskQueue(max_size=1)
    task = Task(task_id="1", task_type="calculate_sum", payload={"values": [1]}, status=TaskStatus.PENDING)
    queue.enqueue(task)
    with pytest.raises(OverflowError):
        queue.enqueue(task)
