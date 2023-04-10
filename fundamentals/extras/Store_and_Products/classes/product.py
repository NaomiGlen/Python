class Product:
    def __init__(self, p_name, type, price):
        self.p_name = p_name
        self.type = type
        self.price = price

    def print_info(self):
        print(self.p_name, self.type, self.price)
        return self

    def update_price(self, percent_change, is_increased):
        if is_increased == True:
            self.price += percent_change
        else:
            self.price -= percent_change
        return self
