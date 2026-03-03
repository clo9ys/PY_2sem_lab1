from src.models import Task

class GenerationTaskSource:
    """ Имитация поступающих задач путем простейшего цикла """
    def __init__(self, count: int):
        self.count = count

    def get_tasks(self) -> list[Task]:
        return [Task(id=str(i), payload=f"data_{i}") for i in range(1, self.count+1)]