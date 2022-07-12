import pytest
from src.pycart.Stock.stock import Stock


def test_stock_as_dict(valid_testdata):
    assert Stock().current == valid_testdata


def test_update_stock_as_dict(valid_stock_testdata):
    Stock().update_stock(valid_stock_testdata[0])
    assert valid_stock_testdata[1] == Stock().current


def test_update_stock_as_list(invalid_data_as_list):
    with pytest.raises(TypeError):
        assert Stock().update_stock(invalid_data_as_list) == "Current order flower must be a dictionary"


def test_update_stock_with_float_values(invalid_value_as_float):
    with pytest.raises(ValueError):
        assert Stock().update_stock(invalid_value_as_float) == "No. of flower must be a positive integer"


def test_update_stock_with_nonnumeric_values(invalid_value_as_nonnumeric):
    with pytest.raises(ValueError):
        assert Stock().update_stock(invalid_value_as_nonnumeric) == "No. of flower must be a positive integer"


def test_update_stock_with_with_numeric_keys(invalid_key_as_nonnumeric):
    with pytest.raises(ValueError):
        assert Stock().update_stock(invalid_key_as_nonnumeric) == "flower name must be a string"
