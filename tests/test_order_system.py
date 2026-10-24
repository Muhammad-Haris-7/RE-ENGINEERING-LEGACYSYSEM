import pytest

import legacy_order_system as legacy
import order_system as new

NOTEBOOKS = {'name': 'Notebook', 'category': 'book', 'price': 300, 'qty': 2}
USB = {'name': 'USB Drive', 'category': 'electronics', 'price': 800, 'qty': 1}


def test_regular_customer_no_delivery():
    assert new.order_total([NOTEBOOKS], 'regular', 'none') == 600.00


def test_student_discount_standard_delivery():
    assert new.order_total([NOTEBOOKS, USB], 'student', 'standard') == 1360.00


def test_staff_discount_express_delivery():
    assert new.order_total([USB], 'staff', 'express') == 1010.00


def test_standard_delivery_fee():
    assert new.order_total([NOTEBOOKS], 'regular', 'standard') == 700.00


def test_express_delivery_fee():
    assert new.order_total([NOTEBOOKS], 'regular', 'express') == 850.00


def test_negative_price_raises_value_error():
    bad = {'name': 'Pen', 'category': 'other', 'price': -50, 'qty': 1}
    with pytest.raises(ValueError):
        new.order_total([bad], 'regular', 'none')


def test_negative_quantity_raises_value_error():
    bad = {'name': 'Pen', 'category': 'other', 'price': 50, 'qty': -1}
    with pytest.raises(ValueError):
        new.order_total([bad], 'regular', 'none')


# Before/after comparison: same input, legacy vs refactored
@pytest.mark.parametrize('customer, delivery', [
    ('student', 'standard'),
    ('regular', 'none'),
    ('staff', 'express'),
    ('student', 'express'),
    ('staff', 'standard'),
])
def test_refactored_matches_legacy(customer, delivery):
    items = [NOTEBOOKS, USB]
    assert new.order_total(items, customer, delivery) == \
        legacy.order_total(items, customer, delivery)


def test_receipt_text_unchanged():
    items = [NOTEBOOKS, USB]
    assert new.print_receipt(items, 'student', 'standard') == \
        legacy.print_receipt(items, 'student', 'standard')