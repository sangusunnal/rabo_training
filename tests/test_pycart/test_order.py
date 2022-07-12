import pytest
from src.pycart.Order.order import Order, InsufficientException


def test_stock_as_dict(valid_testdata):
    assert Order().current == valid_testdata


def test_place_order_as_dict(valid_order_testdata):
    Order().place_order(valid_order_testdata[0])
    assert valid_order_testdata[1] == Order().current


def test_place_order_as_list(invalid_data_as_list):
    with pytest.raises(TypeError):
        assert Order().place_order(invalid_data_as_list) == "Current order flower must be a dictionary"


def test_place_order_with_float_values(invalid_value_as_float):
    with pytest.raises(ValueError):
        assert Order().place_order(invalid_value_as_float) == "No. of flower must be a positive integer"


def test_place_order_with_nonnumeric_values(invalid_value_as_nonnumeric):
    with pytest.raises(ValueError):
        assert Order().place_order(invalid_value_as_nonnumeric) == "No. of flower must be a positive integer"


def test_place_order_with_numeric_keys(invalid_key_as_nonnumeric):
    with pytest.raises(ValueError):
        assert Order().place_order(invalid_key_as_nonnumeric) == "flower name must be a string"


def test_place_order_of_insufficient_stock(invalid_insufficient_stock_data):
    with pytest.raises(InsufficientException):
        assert Order().place_order(invalid_insufficient_stock_data) == "Insufficient Stock"


def test_place_order_non_existing_flower(invalid_new_stock_data):
    with pytest.raises(InsufficientException):
        assert Order().place_order(invalid_new_stock_data) == "No Stock. New flower Request"
