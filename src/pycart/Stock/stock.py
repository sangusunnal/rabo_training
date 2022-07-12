from src.pycart.Stock.constants import INPUT_DATA_DIR
from src.pycart.Fileoperation import fileoperation


class Stock:
    def __init__(self):
        stock = fileoperation.get_data(INPUT_DATA_DIR)
        if stock is None:
            self.current = {}
        else:
            if not isinstance(stock, dict):
                raise TypeError("Input stock must be a dictionary")
            for flower in stock:
                if not isinstance(flower, str):
                    raise ValueError("Flower name must be a string")
                if not isinstance(stock[flower.lower()], int) or stock[flower.lower()] < 0:
                    raise ValueError("No. of flower must be a positive integer")
            self.current = stock

    def update_stock(self, new_stock):
        """
        This Function is Used to update shop stock
        and it will return the current stock with update.
        :param new_stock:
        :return current stock with update:
        """
        if not isinstance(new_stock, dict):
            raise TypeError("Input stock must be a dictionary")
        for flower in new_stock:
            if not isinstance(flower, str):
                raise ValueError("flower name must be a string")
            if not isinstance(new_stock[flower], int) or new_stock[flower] < 0:
                raise ValueError("No. of flower must be a positive integer")
            if flower.lower() in self.current:
                self.current[flower.lower()] += new_stock[flower]
            else:
                self.current[flower.lower()] = new_stock[flower]
        fileoperation.update_data(INPUT_DATA_DIR, self.current)
