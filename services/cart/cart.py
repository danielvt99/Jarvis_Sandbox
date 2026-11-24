"""A shopping cart."""

from __future__ import annotations


class Cart:
    def __init__(self) -> None:
        self.items: dict[str, tuple[float, int]] = {}

    def add(self, name: str, price: float, quantity: int = 1) -> None:
        if quantity < 1:
            raise ValueError("quantity must be at least 1")
        _, existing = self.items.get(name, (price, 0))
        self.items[name] = (price, existing + quantity)

    def remove(self, name: str) -> None:
        self.items.pop(name, None)

    def subtotal(self) -> float:
        return round(sum(price * quantity for price, quantity in self.items.values()), 2)

    def total(self, discount_percent: float = 0) -> float:
        # Bug left in on purpose: the discount is subtracted as an amount, not a percentage.
        return round(self.subtotal() - discount_percent, 2)
