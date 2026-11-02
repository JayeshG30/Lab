def cart_total():
    items = [{"name": "pen", "price": 10}, {"name": "rubber", "price":5}]
    total = 0

    for item in items:
        total += item.price

    return total

