from models import Task
from dataclasses import dataclass, asdict
from logger import make_logger

logger = make_logger()

@dataclass
class ApiTask:
    """Данные задачи из API-заглушки. Содержит id и все возможные поля"""
    id: str
    type: str
    source_endpoint: str | None = None
    source: str | None = None
    format: str | None = None
    recipient: str | None = None


class ApiTaskSource:
    """Имитирует внешний API. Возвращает задачи, как будто они пришли по сети"""
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
        logger.info(f"Данные из API прочитаны, получено {len(result)} задач")
        return result