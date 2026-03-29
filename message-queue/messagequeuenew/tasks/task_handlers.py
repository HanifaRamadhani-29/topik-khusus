from typing import Dict, Any

from tasks.task_models import Task


def handle_resize_image(task: Task) -> str:
    """Simulate an image resize operation based on task payload."""
    payload = task.payload
    source_path = payload.get("image_path")
    dimensions = payload.get("dimensions")

    if not source_path or not isinstance(source_path, str):
        raise ValueError("resize_image task requires a valid image_path")
    if not dimensions or not isinstance(dimensions, dict):
        raise ValueError("resize_image task requires dimensions as a dictionary")

    width = dimensions.get("width")
    height = dimensions.get("height")
    if not isinstance(width, int) or not isinstance(height, int):
        raise ValueError("resize_image dimensions must include integer width and height")

    return f"resized {source_path} to {width}x{height}"


def handle_calculate_sum(task: Task) -> int:
    """Calculate the sum of numeric values in task payload."""
    values = task.payload.get("values")
    if not isinstance(values, list) or not values:
        raise ValueError("calculate_sum task requires a non-empty values list")

    total = 0
    for item in values:
        if not isinstance(item, (int, float)):
            raise ValueError("calculate_sum payload must contain only numbers")
        total += item

    return total


def handle_convert_file(task: Task) -> str:
    """Simulate file conversion and return the resulting target path."""
    payload = task.payload
    source_path = payload.get("file_path")
    target_format = payload.get("target_format")

    if not source_path or not isinstance(source_path, str):
        raise ValueError("convert_file task requires a valid file_path")
    if not target_format or not isinstance(target_format, str):
        raise ValueError("convert_file task requires a target_format string")

    return f"converted {source_path} to .{target_format}" 


TASK_HANDLER_MAP = {
    "resize_image": handle_resize_image,
    "calculate_sum": handle_calculate_sum,
    "convert_file": handle_convert_file,
}


def execute_task(task: Task) -> Any:
    """Dispatch a task to its handler and return the result."""
    handler = TASK_HANDLER_MAP.get(task.task_type)
    if handler is None:
        raise ValueError(f"Unsupported task type: {task.task_type}")
    return handler(task)
