import pytest

from src.product_classes import LawnGrass, Smartphone


def test_smartphone1(smartphone1: Smartphone) -> None:
    assert smartphone1.name == "Iphone 15"
    assert smartphone1.color == "Gray space"


def test_lawn_grass(lawn_grass1: LawnGrass) -> None:
    assert lawn_grass1.quantity == 20


def test_add_error(lawn_grass1: LawnGrass, smartphone1: Smartphone) -> None:
    with pytest.raises(TypeError):
        lawn_grass1 + smartphone1
