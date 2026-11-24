import pytest

from cart import Cart


def test_add_and_subtotal():
    cart = Cart()
    cart.add("tea", 4.50, 2)
    cart.add("mug", 12.00)
    assert cart.subtotal() == 21.00


def test_adding_the_same_item_increases_quantity():
    cart = Cart()
    cart.add("tea", 4.50)
    cart.add("tea", 4.50, 2)
    assert cart.items["tea"] == (4.50, 3)


def test_remove():
    cart = Cart()
    cart.add("tea", 4.50)
    cart.remove("tea")
    assert cart.subtotal() == 0


def test_quantity_must_be_positive():
    with pytest.raises(ValueError):
        Cart().add("tea", 4.50, 0)


def test_discount_is_a_percentage():
    cart = Cart()
    cart.add("mug", 200.00)
    assert cart.total(discount_percent=10) == 180.00
