import json
from src.models import Task

class FileTaskSource:
    """ Имитация поступления задач из файла json"""
    def __init__(self, filepath: str):
        self.filepath = filepath

    def get_tasks(self) -> list[Task]:
        try:
            with open(self.filepath, 'r', encoding="utf-8") as f:
                data = json.load(f) # список словарей с задачами

            return [Task(id=item["id"], payload=item["payload"]) for item in data]

        except FileNotFoundError:
            raise RuntimeError(f"Cannot found file: {self.filepath}")