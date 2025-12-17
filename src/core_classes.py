class Product:
    """
    Класс для представления товара в магазине.

    Attributes:
        name (str): название товара
        description (str): описание товара
        price (float): цена товара
        quantity (int): количество товара на складе
    """

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Category:
    """
    Класс для представления категории товаров.

    Attributes:
        name (str): название категории
        description (str): описание категории
        products (list[Product]): список товаров в категории
        product_count (int): общее количество товаров во всех категориях (классовый атрибут)
        category_count (int): общее количество созданных категорий (классовый атрибут)
    """

    name: str
    description: str
    products: list[Product]
    product_count: int = 0
    category_count: int = 0

    def __init__(self, name: str, description: str, products: list[Product]):
        self.name = name
        self.description = description
        self.products = products if products else []
        Category.product_count += len(products) if products else 0
        Category.category_count += 1
