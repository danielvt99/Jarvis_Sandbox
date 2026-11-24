"""Order totals."""

VAT_RATE = 0.15


def order_total(subtotal: float, shipping: float = 0) -> float:
    return round(subtotal * (1 + VAT_RATE) + shipping, 2)
