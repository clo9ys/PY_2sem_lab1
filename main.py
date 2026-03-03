from src import FileTaskSource, GenerationTaskSource, ApiTaskSource
from src.protocol import TaskSource
from src.logger import make_logger

def process_task(source) -> None:
    if not isinstance(source, TaskSource):
        raise TypeError(f"Object {source} doesn't comply with the protocol - missing method get_tasks")

    tasks = source.get_tasks()
    for task in tasks:
        print(f'Task processing {task.id}: {task.payload}')

if __name__ == "__main__":
    try:
        process_task(FileTaskSource("tasks.json"))
        process_task(GenerationTaskSource(5))
        process_task(ApiTaskSource())
    except RuntimeError as err:
        print(err)
    except TypeError as err:
        print(err)