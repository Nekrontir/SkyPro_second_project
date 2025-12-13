class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Category:
    name: str
    description: str
    products: list[Product]
    product_count: int = 0
    category_count: int = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products if products else []
        Category.product_count += len(products) if products else 0
        Category.category_count += 1
