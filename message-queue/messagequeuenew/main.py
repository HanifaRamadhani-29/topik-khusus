import logging
from config.settings import Settings
from consumer.consumer import TaskConsumer
from producer.producer import TaskProducer
from queue.task_queue import TaskQueue
from tasks.task_factory import TaskFactory


def configure_logging(level: str) -> None:
    logging.basicConfig(
        level=level,
        format="%(asctime)s %(levelname)s %(name)s %(message)s",
    )


def build_sample_tasks() -> list[dict]:
    return [
        {
            "task_type": "resize_image",
            "payload": {"image_path": "image.jpg", "dimensions": {"width": 800, "height": 600}},
        },
        {
            "task_type": "calculate_sum",
            "payload": {"values": [10, 20, 30]},
        },
        {
            "task_type": "convert_file",
            "payload": {"file_path": "report.docx", "target_format": "pdf"},
        },
    ]


def main() -> None:
    settings = Settings()
    settings.validate()
    configure_logging(settings.log_level)

    queue = TaskQueue(max_size=settings.queue_max_size)
    factory = TaskFactory(settings.allowed_task_types)
    producer = TaskProducer(queue, factory)
    consumer = TaskConsumer(queue, settings.retry_limit)

    for task_data in build_sample_tasks():
        producer.submit_task(task_data["task_type"], task_data["payload"])

    consumer.process_all(max_iterations=settings.worker_batch_size)


if __name__ == "__main__":
    main()
