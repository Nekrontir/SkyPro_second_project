from typing import Any, Dict, List, Union


class Product:
    """
    Класс для представления товара в магазине.
    """

    name: str
    description: str
    quantity: int
    all_products: list = []

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        Product.all_products.append(self)

    @classmethod
    def new_product(cls, dictionary: Dict[Any, Any]) -> Any:
        for product in cls.all_products:
            if product.name == dictionary.get("name"):
                product.quantity += dictionary["quantity"]
                if product.__price < dictionary.get("price"):
                    product.__price = dictionary.get("price")
                return product

        return cls(
            dictionary["name"],
            dictionary["description"],
            dictionary["price"],
            dictionary["quantity"],
        )

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, value: float) -> None:
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        elif value < self.__price:
            answer = input("Подтвердить снижение цены (y/n): ")
            if answer == "y":
                self.__price = value
        else:
            self.__price = value

    def __str__(self) -> str:
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: Any) -> Any:
        return self.__price * self.quantity + other.price * other.quantity


class Category:
    """
    Класс для представления категории товаров.
    """

    name: str
    description: str
    product_count: int = 0
    category_count: int = 0

    def __init__(self, name: str, description: str, products: Union[List[Product], None]):
        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.product_count += len(products) if products else 0
        Category.category_count += 1

    @property
    def products(self) -> str:
        products_list = ""
        for product in self.__products:
            products_list += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return products_list

    def add_product(self, product: Product) -> None:
        self.__products.append(product)
        Category.product_count += 1

    def __str__(self) -> str:
        total_number: int = 0
        for product in self.__products:
            total_number += product.quantity
        return f"{self.name}, количество продуктов: {total_number} шт."
