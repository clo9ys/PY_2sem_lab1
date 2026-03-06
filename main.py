import json

from src import FileTaskSource, GenerationTaskSource, ApiTaskSource
from src.protocol import TaskSource
from src.logger import make_logger

logger = make_logger()

def process_task(source) -> None:
    """Проверяет источник, получает задачи и печатает их. Если источник не подходит, выбрасывает ошибку"""
    if not isinstance(source, TaskSource):
        raise TypeError(f"Объект не реализует единый контракт - отсутствует метод get_tasks()")

    tasks = source.get_tasks()
    for task in tasks:
        logger.info(f'Выполнение задачи {task.id}: {task.payload}')
        print(f'Выполнение задачи {task.id}: {task.payload}')

if __name__ == "__main__":
    try:
        process_task(FileTaskSource("tasks.json"))
        process_task(GenerationTaskSource(5))
        process_task(ApiTaskSource())
    except FileNotFoundError as err:
        logger.error(err)
        print(err)
    except json.JSONDecodeError as err:
        logger.error(err)
        print(err)
    except TypeError as err:
        logger.error(err)
        print(err)