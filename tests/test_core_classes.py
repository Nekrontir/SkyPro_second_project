from unittest.mock import patch

from _pytest.capture import CaptureFixture

from src.core_classes import Category, Product


def test_product1(product1: Product) -> None:
    assert product1.name == "Samsung Galaxy S23 Ultra"
    assert product1.price == 180000.0
    assert product1.description == "256GB, Серый цвет, 200MP камера"
    assert product1.quantity == 5


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


def test_category3(category2: Category) -> None:
    assert category2.products == '55" QLED 4K, 123000.0 руб. Остаток: 7 шт.\n'


def test_product_creation_and_price_setter(product1: Product, capsys: CaptureFixture[str]) -> None:
    test_cases = [
        (product1.price + 100, product1.price + 100, None),
        (product1.price - 50, product1.price - 50, "y"),
        (product1.price, product1.price, "n"),
    ]
    for new_price, expected_price, mock_input in test_cases:
        if mock_input:
            with patch("builtins.input", return_value=mock_input):
                product1.price = new_price
        else:
            product1.price = new_price
        assert product1.price == expected_price


def test_category_methods(category2: Category) -> None:
    new_product = Product("New", "Desc", 50.0, 5)
    category2.add_product(new_product)
    assert new_product.name in category2.products


def test_new_product_method(product1: Product) -> None:
    assert product1.price == 180_000
    new_product = Product.new_product(
        {
            "name": "Samsung Galaxy S23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 200_000,
            "quantity": 10,
        }
    )
    assert new_product.quantity == 15
    assert new_product.price == 200_000
    assert product1.price == 200_000


def test_category_with_edge_cases() -> None:
    cat1 = Category("Empty", "Desc", [])
    assert cat1.products == ""
    cat2 = Category("None", "Desc", [])
    assert cat2.products == ""


def test_creation() -> None:
    p1 = Product("P1", "Desc1", 100.0, 5)
    p2 = Product("P2", "Desc2", 200.0, 3)
    category = Category("Cat", "Desc", [p1])
    category.add_product(p2)
    assert p1 in Product.all_products
    assert p2 in Product.all_products
    assert p1.name in category.products
    assert p2.name in category.products
