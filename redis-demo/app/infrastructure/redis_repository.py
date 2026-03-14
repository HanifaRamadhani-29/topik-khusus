import redis
from app.domain.task import Task
from app.interfaces.task_repository import TaskRepository

class RedisRepository(TaskRepository):
    def __init__(self, host: str = "localhost", port: int = 6379, db: int = 0):
        self.client = redis.Redis(host=host, port=port, db=db, decode_responses=True)

    def _key(self, task_id: str) -> str:
        return f"task:{task_id}"

    def save(self, task: Task) -> Task:
        key = self._key(task.id)
        payload = {"id": task.id, "title": task.title, "completed": str(task.completed)}
        # Example Redis set operation (hash set):
        self.client.hset(key, mapping=payload)
        # Also store a simple string for example get
        self.client.set(f"task-title:{task.id}", task.title)
        return task

    def get(self, task_id: str) -> Task | None:
        key = self._key(task_id)
        data = self.client.hgetall(key)
        if not data:
            return None
        title_from_cache = self.client.get(f"task-title:{task_id}")
        if title_from_cache is not None:
            data["title"] = title_from_cache
        return Task(
            id=data.get("id"),
            title=data.get("title"),
            completed=(data.get("completed") == "True"),
        )
