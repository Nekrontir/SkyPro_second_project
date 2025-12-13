from src.core_classes import Category, Product


def test_product1(product1: Product) -> None:
    assert product1.name == "Samsung Galaxy S23 Ultra"
    assert product1.price == 180000.0
    assert product1.description == "256GB, Серый цвет, 200MP камера"
    assert product1.quantity == 5


def test_product2(product2: Product) -> None:
    assert product2.name == "Iphone 15"
    assert product2.price == 210000.0
    assert product2.description == "512GB, Gray space"
    assert product2.quantity == 8


def test_product3(product3: Product) -> None:
    assert product3.name == "Xiaomi Redmi Note 11"
    assert product3.price == 31000.0
    assert product3.description == "1024GB, Синий"
    assert product3.quantity == 14


def test_category1(category1: Category) -> None:
    assert category1.name == "Смартфоны"
    assert category1.description == "Смартфоны - удобство для жизни"
    assert category1.product_count == 3
    assert category1.category_count == 1


def test_category2(category2: Category) -> None:
    assert category2.name == "Телевизоры"
    assert category2.description == "Современный телевизор, который позволяет наслаждаться просмотром"
    assert category2.product_count == 1
    assert category2.category_count == 1
