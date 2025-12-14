import json
import os
from typing import Any

from src.core_classes import Category, Product

# path_to_json = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))),"data", 'products.json')


def read_json(path: str) -> Any:
    full_path = os.path.abspath(path)
    with open(full_path, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data


def create_objects_from_json(data: list) -> list:
    objects: list = []
    for category in data:
        products: list = []
        for product in category["products"]:
            products.append(Product(**product))
        category["products"] = products
        objects.append(Category(**category))
    return objects


if __name__ == "__main__":

    raw_data = read_json("../data/products.json")
    print(type(raw_data))
    print(raw_data)
    objects = create_objects_from_json(raw_data)
    print(objects[1].name, "\n")
    print(objects[1].description, "\n")
    print(objects[1].products, "\n")
