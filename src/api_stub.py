from src.models import Task
from dataclasses import dataclass, asdict

@dataclass
class ApiTask:
    id: str
    type: str
    source_endpoint: str | None = None
    source: str | None = None
    format: str | None = None
    recipient: str | None = None


class ApiTaskSource:
    def __init__(self, endpoint: str="http://api-stub/tasks"):
        self.endpoint = endpoint

    def get_tasks(self) -> list[Task]:
        result = []
        api_tasks = [
            ApiTask(id="report67", type="report", format="docx", source_endpoint=self.endpoint),
            ApiTask(id="backup_52", type="backup", source="postgres_main", source_endpoint=self.endpoint),
            ApiTask(id="msg13", type="send_message", recipient="somebody13", source_endpoint=self.endpoint),
        ]
        for task in api_tasks:
            payload_dict = asdict(task)
            del payload_dict["id"]
            result.append(Task(id=task.id, payload=payload_dict))
        return result