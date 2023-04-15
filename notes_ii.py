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

##ERD/SQL

#Examples of One-to-One
#Customers and Credit Cards - 
#Every Customer has one Credit Card, 
#every Credit Card belongs to one Customer.

#User and Email - Every User has one Email Address,
# every Email Address has one User.

#Product and Image - Every Product has an Image,
# every Image is of a Product.

#Examples of One-to-Many
#Messages and Comments - 
# One Comment belongs to one Message, 
#but one Message can have many Comments.

#States and Cities - One City is only in one State,
#but one State can have many Cities.

#Customers and Orders - One Order only has one Customer,
#but one Customer can have many Orders.

#Examples of Many-to-Many
#Users and Interests - One User can have many Interests,
#one Interest can be applied to many Users.

#Actors and Movies - One Movie can have many Actors,
# one Actor can be in many Movies.

#Businesses and Cities - One Business can be spread across 
#many Cities, one City can be home to many Businesses.

#MySQL
#Select all method - selecting data from a table
#SELECT *(all) FROM (table_name);
#Select one method
#SELECT (column) FROM (table_name);
#Select with conditionals
#SELECT *(all) FROM (table_name) WHERE (column) = (value)
#Select with sorting
#SELECT *(all) FROM (table_name) ORDER BY (value) DESC(descending)/ASC(ascending);


#Insert method - inserting(adding) data to a table
#INSERT INTO table_name (column_name1, column_name2) 
#VALUES('column1_value', 'column2_value');

#Update records method - updating information in a table
#UPDATE table_name
#SET column1 = value1, column2 = value, ...
#WHERE condition;

#Delete records method - IMPORTANT! if WHERE condition is not added to the DELETE statement, it will delete all the records on the table.
#DELETE FROM table_name WHERE condition;