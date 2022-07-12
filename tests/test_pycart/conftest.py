import pytest


stock_data = [({"rose": 138, "lily": 70, "tulip": 100, "orchid": 90, "carnation": 196})]
order_valid_data = [
    ({"tulip": 2, "lily": 1}, {"rose": 138, "lily": 69, "tulip": 98, "orchid": 90, "carnation": 196}),
    ({"Rose": 100, "lily": 3}, {"rose": 38, "lily": 66, "tulip": 98, "orchid": 90, "carnation": 196}),
    ({"tulip": 2, "carnation": 80}, {"rose": 38, "lily": 66, "tulip": 96, "orchid": 90, "carnation": 116}),
    ({"tulip": 2, "carnation": 10, "orchid": 88}, {"rose": 38, "lily": 66, "tulip": 94, "orchid": 2, "carnation": 106}),
    ({"rose": 38, "carnation": 106, "orchid": 2, "tulip": 94},
     {"rose": 0, "lily": 66, "tulip": 0, "orchid": 0, "carnation": 0})]

stock_valid_data = [
    ({"tulip": 2, "lily": 1, "Aster": 10},
     {"rose": 138, "lily": 71, "tulip": 102, "orchid": 90, "carnation": 196, "aster": 10}),
    ({"Rose": 100, "lily": 3}, {"rose": 238, "lily": 74, "tulip": 102, "orchid": 90, "carnation": 196, "aster": 10}),
    ({"tulip": 2, "carnation": 80},
     {"rose": 238, "lily": 74, "tulip": 104, "orchid": 90, "carnation": 276, "aster": 10}),
    ({"Aster": 2, "carnation": 10, "orchid": 88},
     {"rose": 238, "lily": 74, "tulip": 104, "orchid": 178, "carnation": 286, "aster": 12}),
    ({"rose": 0, "lily": 0, "tulip": 0, "orchid": 0, "carnation": 0},
     {"rose": 238, "lily": 74, "tulip": 104, "orchid": 178, "carnation": 286, "aster": 12})]
data_as_list = [
    ([{"tulip": 2, "lily": 1}]),
    (["Rose", "lily"]),
    ([["tulip"], "carnation"]),
    ([10, 56, 90]),
    ([{}]), ]

data_value_as_float = [
    ({"orchid": 0.0, "lily": 9.7}),
    ({"tulip": 177.0, "carnation": 5.90}),
    ({"tulip": 1.000, "carnation": 0}),
    ({"rose": 1.999, "lily": 6.9, "tulip": 89., "orchid": 90., "carnation": 1.00}),
    ({"tulip": 8.9, "carnation": 4.56000, "lily": 45.98}), ]

data_value_as_nonnumeric = [
    ({"orchid": '1', "carnation": 9.7}),
    ({"tulip": 'tulip', "carnation": 5}),
    ({"orchid": '1.000', "rose": 56}),
    ({"rose": 1.999, "lily": 6, "tulip": "", "orchid": 90, "carnation": "00"}),
    ({"tulip": "8.9$", "carnation": "4.56000", "": 45.98}),

]
data_key_as_numeric = [
    ({1: '1', "carnation": 9}),
    ({455: 'tulip', 5: 5}),
    ({1.99: 1.000, 0: 56}),
    ({"rose": 1.999, "lily": 6, 567798: "", "orchid": 90, "carnation": "00"}),
    ({45: 45, "carnation": "4.56000", "rose": 45}),

]
insufficient_stock_data = [
    ({"orchid": 4566, "carnation": 8000}),
    ({"tulip": 500, "carnation": 5}),
    ({"tulip": 1, "carnation": 8900}),
    ({"rose": 1370, "lily": 6, "tulip": 1000, "orchid": 901, "carnation": 198}),
    ({"tulip": 4555, "carnation": 8000}),

]
new_stock_data = [
    ({"orchid": 1, "sunflower": 10}),
    ({"tulips": 56, "carnation": 5}),
    ({"tulip": 1, "leek": 56}),
    ({"daisy": 5, "lily": 6, "tulip": 4, "orchid": 90, "carnation": 7}),
    ({"tulip": 7, "carnation": 4, "Aster": 5}), ]


@pytest.fixture(scope="module", params=stock_data)
def valid_testdata(request):
    test_data = request.param
    return test_data


@pytest.fixture(scope="module", params=order_valid_data)
def valid_order_testdata(request):
    test_data = request.param
    return test_data


@pytest.fixture(scope="module", params=stock_valid_data)
def valid_stock_testdata(request):
    test_data = request.param
    return test_data


@pytest.fixture(scope="module", params=data_as_list)
def invalid_data_as_list(request):
    test_data = request.param
    return test_data


@pytest.fixture(scope="module", params=data_value_as_float)
def invalid_value_as_float(request):
    test_data = request.param
    return test_data


@pytest.fixture(scope="module", params=data_value_as_nonnumeric)
def invalid_value_as_nonnumeric(request):
    test_data = request.param
    return test_data


@pytest.fixture(scope="module", params=data_key_as_numeric)
def invalid_key_as_nonnumeric(request):
    test_data = request.param
    return test_data


@pytest.fixture(scope="module", params=insufficient_stock_data)
def invalid_insufficient_stock_data(request):
    test_data = request.param
    return test_data


@pytest.fixture(scope="module", params=new_stock_data)
def invalid_new_stock_data(request):
    test_data = request.param
    return test_data
