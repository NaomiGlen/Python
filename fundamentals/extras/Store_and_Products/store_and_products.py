class Store:
    def __init__(self, name, products):
        self.name = name
        self.products = products
        products = []

    def add_product(self,new_product):
        pass
    def sell_product(self,id):
        pass
    def inflation(self,percent_increase):
        pass
    def set_clearance(self,category,percent_discout):
        pass

class Product:
    def __init__(self, product_name, price, category):
        self.product_name = product_name
        self.price = price
        self.category = category

    def update_price(self, percent_change,is_increased):
        pass
    def print_info(self):
        print(f'Product:{self.product_name}, Cost:${self.price}, Category:{self.category}')

bananas = Product("Bananas", 2.99, "Produce")
bananas.print_info()

milk = Product("Milk", 4.59,"Dairy")
milk.print_info()

cereal = Product("Cereal", 3.99, "Grocery")
cereal.print_info()

chicken = Product("Whole Chicken", 6.99,"Poultry")
