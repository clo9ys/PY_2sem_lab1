from dataclasses import dataclass
from typing import Any

@dataclass
class Task:
    """Модель задачи. Содержит id и любые данные в payload"""
    id: str
    payload: Any # данные могут быть любого типа