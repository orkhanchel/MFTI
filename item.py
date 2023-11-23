import json
import random

class Item:
    _items = {}

    def __init__(self, item_id, name, price):
        self.item_id = item_id
        self.name = name
        self.price = price
        Item._items[item_id] = self

    def __hash__(self):
        return hash(self.item_id)

    @staticmethod
    def generate_random_item():
        item_id = len(Item._items) + 1
        name = f"Item_{item_id}"
        price = random.uniform(10, 100)
        return Item(item_id, name, price)

    @classmethod
    def create_from_json(cls, json_path):
        with open(json_path, 'r') as file:
            data = json.load(file)
            return cls(data['item_id'], data['name'], data['price'])

    def save_as_json(self):
        data = {'item_id': self.item_id, 'name': self.name, 'price': self.price}
        with open(f"{self.name}.json", 'w') as file:
            json.dump(data, file)


