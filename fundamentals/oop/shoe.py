class Shoe:
    def __init__(self, brand, shoe_type, price):
        self.brand = brand
        self.type = shoe_type
        self.price = price
        self.in_stock = True
    def on_sale_by_percent(self,percent_off):
        self.price = self.price * (1-percent_off) 
        #takes a float/percent as an arguement and reduces the 
        #price of the item by that percentage.
    def total_with_tax(self, tax_rate):
        tax = self.price * tax_rate
        total = self.price + tax
        return total
        #Returns a total with tax added to the price.
    def cut_price_by(self,amount):
        if amount < self.price:
            self.price -= amount
        else:
            print("Price deduction too large.")
        #Reduces the price by a fixed dollar amount.

skater_shoe = Shoe("Vans", "Low-top Trainers", 59.99)
dress_shoe = Shoe("Jack & Jill Bootery", "Ballet Flats", 29.99)

print(skater_shoe.type)
print(dress_shoe.type)

skater_shoe.price = skater_shoe.price * (1-0.2)
dress_shoe.price = dress_shoe.price * (1-0.2)
skater_shoe.price = skater_shoe.price * (1-0.1)