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
    all_products = []

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        Product.all_products.append(self)

    @classmethod
    def new_product(cls, dictionary: dict):
        for product in cls.all_products:
            if product.name == dictionary.get("name"):
                product.quantity += dictionary["quantity"]
                if product.__price < dictionary.get("price"):
                    product.__price = dictionary.get("price")
                    return cls(
                        product.name,
                        product.description,
                        product.__price,
                        product.quantity,
                    )
            else:
                return cls(
                    dictionary.get("name"),
                    dictionary.get("description"),
                    dictionary.get("price"),
                    dictionary.get("quantity"),
                )
        return cls

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        elif value < self.__price:
            answer = input("Подтвердить снижение цены (y/n): ")
            if answer == "y":
                self.__price = value


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
        self.__products = products if products else []
        Category.product_count += len(products) if products else 0
        Category.category_count += 1

    @property
    def products(self):
        products_list = ""
        for product in self.__products:
            products_list += f"{product.name}, {product.price}. Остаток: {product.quantity}\n"
        return products_list

    def add_product(self, product: Product):
        self.__products.append(product)
        Category.product_count += 1
