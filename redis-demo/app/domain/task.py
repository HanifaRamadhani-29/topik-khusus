class Task:
    def __init__(self, id: str, title: str, completed: bool = False):
        self.id = str(id)
        self.title = title
        self.completed = completed

    def to_dict(self):
        return {"id": self.id, "title": self.title, "completed": self.completed}

    @classmethod
    def from_dict(cls, data: dict):
        return cls(id=data.get("id"), title=data.get("title"), completed=data.get("completed", False))
