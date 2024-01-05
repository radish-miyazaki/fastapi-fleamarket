from enum import Enum
from typing import Optional


class ItemStatus(Enum):
    ON_SALE = 'ON_SALE'
    SOLD_OUT = 'SOLD_OUT'


class Item:
    def __init__(
            self,
            id: int,
            name: str,
            price: int,
            description: Optional[str],
            status: ItemStatus
    ):
        self.id = id
        self.name = name
        self.price = price
        self.description = description
        self.status = status


items = [
    Item(1, 'PC', 100000, '美品です', ItemStatus.ON_SALE),
    Item(2, 'スマートフォン', 50000, None, ItemStatus.ON_SALE),
    Item(3, 'Python本', 1000, '使用感あり', ItemStatus.SOLD_OUT)
]


def find_all():
    return items


def find_by_id(id: int):
    for item in items:
        if item.id == id:
            return item

    return None


def find_by_name(name: str):
    filtered_items = []

    for item in items:
        if name in item.name:
            filtered_items.append(item)

    return filtered_items
