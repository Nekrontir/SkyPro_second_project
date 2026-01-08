from _pytest.capture import CaptureFixture

from src.core_classes import Product


def test_mixin(capsys: CaptureFixture[str]) -> None:
    prod = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    assert prod.name == "Iphone 15"
    captured = capsys.readouterr()
    assert captured.out == "Product(Iphone 15, 512GB, Gray space, 210000.0, 8)\n"
