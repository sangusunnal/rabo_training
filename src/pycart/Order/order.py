from src.pycart.Fileoperation import fileoperation
from src.pycart.Stock.constants import INPUT_DATA_DIR


class InsufficientException(Exception):
    pass


class Order:
    def __init__(self):
        stock = fileoperation.get_data(INPUT_DATA_DIR)
        if stock is None:
            self.current = {}
        else:
            self.current = stock
        self.cart = []

    def place_order(self, current_order):
        """
        This Function is Used to place the current order
        and it will return the current stock.
        :param current_order:
        :return current stock:
        """
        if not isinstance(current_order, dict):
            raise TypeError("Current order flower must be a dictionary")
        for flower in current_order:
            if not isinstance(flower, str):
                raise ValueError("flower name must be a string")
            if not isinstance(current_order[flower], int) or current_order[flower] < 0:
                raise ValueError("No. of flower must be a positive integer")
            if flower.lower() not in self.current:
                raise InsufficientException("No Stock. New flower Request")
            if current_order[flower] > self.current[flower.lower()]:
                raise InsufficientException("Insufficient Stock")
            if flower.lower() in self.current:
                self.current[flower.lower()] -= current_order[flower]
                self.cart.append(current_order)
        fileoperation.update_data(INPUT_DATA_DIR, self.current)

    def check_out(self):
        for orders in self.cart:
            for flowers, qty in orders.items():
                print(flowers, qty)
