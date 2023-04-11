# Base constructor
# declare a class and give it name User
class User:
    def __init__(self):
        self.first_name = "Ada"
        self.last_name = "Lovelace"
        self.age = 42

#Assign a variable to new users in the outer scope
user_ada = User() #follow up new variables with ()
print(user_ada.first_name)

user_2 = User()
print(user_2.first_name)

#Passing in Arguments
class Shoe:
    def __init__(self,brand,shoe_type,price):
        self.brand = brand
        self.type = shoe_type
        self.price = price
        self.in_stock = True
skater_shoe = Shoe("Vans", "Low-top Trainers", 59.99)
dress_shoe = Shoe("Jack & Jill Bootery", "Ballet Flats", 29.99)
print(skater_shoe.type)
print(dress_shoe.type)

#Adding Methonds to Classes
class User:
    def __init__(self,name,email): #Initialization method
        self.name = name
        self.email = email
    def greeting(self):
        print(f"Hello, my name is {self.name}")
#Takes a float/percent as an argument and reduces the 
# price of the item by that percentage.
    def on_sale_by_percent(self,percent_off):
        # ,-----------,-----^ self = shoe instance
        self.price = self.price * (1-percent_off)
#Returns a total with tax added to the price.
    def total_with_tax(self,tax_rate):
        tax = self.price * tax_rate
        total = self.price + tax
        return total
#Reduces the price by a fixed dollar amount. 
    def cut_price_by(self,amount):
        if amount < self.price:
            self.price -= amount
        else:
            print("Price deduction too large")
