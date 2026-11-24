from checkout import order_total


def test_vat_is_added():
    assert order_total(100) == 115.00


def test_shipping_is_added_after_vat():
    assert order_total(100, shipping=50) == 165.00
