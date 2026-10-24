#Order calculator (re-engineered version).




#  Business rules (change rates and fees here only) 
STUDENT_DISCOUNT = 0.10
STAFF_DISCOUNT = 0.05
EXPRESS_FEE = 250
STANDARD_FEE = 100

DISCOUNT_RATES = {
    'student': STUDENT_DISCOUNT,
    'staff': STAFF_DISCOUNT,
}

DELIVERY_FEES = {
    'express': EXPRESS_FEE,
    'standard': STANDARD_FEE,
}


def calculate_subtotal(items):
    """Return the sum of price * qty over all items."""
    subtotal = 0
    for item in items:
        subtotal = subtotal + item['price'] * item['qty']
    return subtotal


def calculate_discount(subtotal, customer_type):
    """Return the discount amount for this customer type (0 if none)."""
    rate = DISCOUNT_RATES.get(customer_type, 0)
    return subtotal * rate


def calculate_delivery_fee(delivery):
    """Return the delivery fee (0 for unknown or no delivery)."""
    return DELIVERY_FEES.get(delivery, 0)


def order_total(items, customer_type, delivery):
    """Return the final order total in PKR, rounded to 2 decimals."""
    subtotal = calculate_subtotal(items)
    discounted = subtotal - calculate_discount(subtotal, customer_type)
    return round(discounted + calculate_delivery_fee(delivery), 2)


def print_receipt(items, customer_type, delivery):
    """Return the receipt text for an order."""
    amount = order_total(items, customer_type, delivery)
    lines = ['ORDER RECEIPT']
    for item in items:
        line_total = item['price'] * item['qty']
        lines.append(f"{item['qty']} x {item['name']} = {line_total}")
    lines.append(f"Customer: {customer_type}")
    lines.append(f"Delivery: {delivery}")
    lines.append(f"Total: {amount}")
    return '\n'.join(lines)


if __name__ == '__main__':
    sample = [
        {'name': 'Notebook', 'category': 'book', 'price': 300, 'qty': 2},
        {'name': 'USB Drive', 'category': 'electronics', 'price': 800, 'qty': 1},
    ]
    print(print_receipt(sample, 'student', 'standard'))