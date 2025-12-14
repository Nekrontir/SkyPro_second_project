from pathlib import Path

from src.utils import create_objects_from_json, read_json


def test_read_json(tmp_path: Path) -> None:
    """
    Проверка чтения json-файла
    :param tmp_path:
    :return: словарь с данными
    """
    test_file = tmp_path / "test.json"
    test_file.write_text('{"test": "test"}')
    assert read_json(str(test_file)) == {"test": "test"}


def test_read_json_file(prod_test_dict: list) -> None:
    ob = create_objects_from_json(prod_test_dict)
    assert ob[0].name == "t1"
    assert ob[1].name == "t2"
    assert ob[0].description == "t"
    assert ob[1].description == "tt"
    assert ob[0].product_count == 4
    assert ob[0].category_count == 2
