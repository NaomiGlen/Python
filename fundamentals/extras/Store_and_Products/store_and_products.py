class Store:
    def __init__(self, name, products):
        self.name = name
        self.products = products
        products = []

    def add_product(self,new_product,amount):
        new_product = self.products
        amount = 0
        return self
    def sell_product(self,id):
        pass


class Product:
    def __init__(self, product_name, price, category):
        self.product_name = product_name
        self.price = price
        self.category = category

    def update_price(self, percent_change,is_increased):
        if is_increased:
            self.price = self.price * (1+percent_change)
            self.price = round(self.price,2)
        else:
            self.price = self.price * (1-percent_change)
            self.price = round(self.price,2)
        return self
    
    def print_info(self):
        print(f'Product:{self.product_name}, Cost:${self.price}, Category:{self.category}')

bananas = Product("Bananas", 2.99, "Produce")
bananas.print_info()

milk = Product("Milk", 4.59,"Dairy")
milk.print_info()

cereal = Product("Cereal", 3.99, "Grocery")
cereal.print_info()

chicken = Product("Whole Chicken", 6.99,"Poultry")
chicken.print_info()

bananas.update_price(0.10,True)
bananas.print_info()

chicken.update_price(0.10,False)
chicken.print_info()