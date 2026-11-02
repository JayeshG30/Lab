import pytest
from cart import cart_total


def test_cart_total_returns_correct_sum():
    """Test that cart_total returns the correct sum of all item prices."""
    assert cart_total() == 15


def test_cart_total_returns_integer():
    """Test that cart_total returns a numeric type."""
    result = cart_total()
    assert isinstance(result, (int, float))


def test_cart_total_is_positive():
    """Test that the cart total is a positive value."""
    assert cart_total() > 0
