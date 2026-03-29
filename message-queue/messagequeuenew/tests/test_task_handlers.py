import pytest

from tasks.task_handlers import execute_task
from tasks.task_models import Task, TaskStatus


def test_calculate_sum_returns_correct_value() -> None:
    task = Task(task_id="1", task_type="calculate_sum", payload={"values": [1, 2, 3]})
    result = execute_task(task)
    assert result == 6


def test_resize_image_requires_valid_payload() -> None:
    task = Task(task_id="2", task_type="resize_image", payload={"dimensions": {"width": 200, "height": 100}})
    with pytest.raises(ValueError, match="image_path"):
        execute_task(task)


def test_convert_file_returns_description() -> None:
    task = Task(task_id="3", task_type="convert_file", payload={"file_path": "doc.md", "target_format": "pdf"})
    result = execute_task(task)
    assert "converted doc.md to .pdf" == result
