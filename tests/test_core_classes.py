

def test_product1(product1):
    assert product1.name == "Samsung Galaxy S23 Ultra"
    assert product1.price == 180000.0
    assert product1.description == "256GB, Серый цвет, 200MP камера"
    assert product1.quantity == 5

def test_product2(product2):
    assert product2.name == "Iphone 15"
    assert product2.price == 210000.0
    assert product2.description == "512GB, Gray space"
    assert product2.quantity == 8

def test_product3(product3):
    assert product3.name == "Xiaomi Redmi Note 11"
    assert product3.price == 31000.0
    assert product3.description == "1024GB, Синий"
    assert product3.quantity == 14
