import pytest

from src.core_classes import Category, Product


@pytest.fixture(autouse=True)
def reset_category_counters() -> None:
    Category.category_count = 0
    Category.product_count = 0


@pytest.fixture
def product1() -> Product:
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)


@pytest.fixture
def product2() -> Product:
    return Product("Iphone 15", "512GB, Gray space", 210000.0, 8)


@pytest.fixture
def product3() -> Product:
    return Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)


# product_1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
# product_2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
# product_3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
# product_4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)


@pytest.fixture
def category1() -> Category:
    product_1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product_2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product_3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    return Category("Смартфоны", "Смартфоны - удобство для жизни", [product_1, product_2, product_3])


@pytest.fixture
def category2() -> Category:
    product_4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    return Category("Телевизоры", "Современный телевизор, который позволяет наслаждаться просмотром", [product_4])


@pytest.fixture
def prod_test_dict() -> list:
    return [
        {
            "name": "t1",
            "description": "t",
            "products": [
                {"name": "pr1", "description": "pr1", "price": 1.01, "quantity": 1},
                {"name": "pr2", "description": "pr2", "price": 2.01, "quantity": 1},
                {"name": "pr3", "description": "pr3", "price": 3.01, "quantity": 1},
            ],
        },
        {
            "name": "t2",
            "description": "tt",
            "products": [{"name": "pr4", "description": "pr4", "price": 4.01, "quantity": 1}],
        },
    ]
