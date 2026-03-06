from models import Task
from logger import make_logger

logger = make_logger()

class GenerationTaskSource:
    """Создает задачи программно с помощью цикла"""
    def __init__(self, count: int):
        self.count = count

    def get_tasks(self) -> list[Task]:
        tasks = [Task(id=str(i), payload=f"data_{i}") for i in range(1, self.count+1)]
        logger.info(f"Сгенерировано {len(tasks)} задач")
        return tasks