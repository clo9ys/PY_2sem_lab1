import json, pytest
from src.file_source import FileTaskSource

def test_file_source_read_json(fs):
    file_path = "/data/tasks.json"
    fs.create_file(file_path, contents=json.dumps([
        {"id": "1", "payload": {"type": "test"}},
        {"id": "2", "payload": "something"}
    ]))

    source = FileTaskSource(file_path)
    tasks = source.get_tasks()
    assert len(tasks) == 2
    assert tasks[0].id == "1" and tasks[1].id == "2"
    assert  tasks[0].payload == {"type": "test"} and tasks[1].payload == "something"


def test_file_not_found_error():
    source = FileTaskSource("random/path")
    with pytest.raises(FileNotFoundError, match="не найден"):
        source.get_tasks()


def test_file_source_invalid_json(fs):
    file_path = "/data/invalid.json"
    fs.create_file(file_path, contents="this is not json")

    source = FileTaskSource(file_path)
    with pytest.raises(json.JSONDecodeError, match="некорректный JSON"):
        source.get_tasks()