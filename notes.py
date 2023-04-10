#Dictionaries are defined with curly brackets. Indexed by Key: Value Pairs. Can contain nested sequences
#person = {
#    "first": "Ada",
#    "last": "Lovelace",
#    "age": 42,
#    "is_organ_donor": True
#}
# Adds a new key value pair for email to person
#person["email"] = "alovelace@codingdojo.com"
        
# Changes person's "last" value to "Bobada"
#person["last"] = "Bobada"
#print(person)

#if "email" not in person:
#    person["email"] = "newemail@email.com"
#else:
#    print("Would you like to replace your existing email?")

#print(person["first_name"])
#full_name = person["first_name"] + " " + person["last_name"]

#my_dict = { "name": "Noelle", "language": "Python" }
#for each_key in my_dict:
#    print(each_key)
# output: name, language (in this case it would be Noelle, Python)

#capitals = {"Washington":"Olympia","California":"Sacramento","Idaho":"Boise","Illinois":"Springfield","Texas":"Austin","Oklahoma":"Oklahoma City","Virginia":"Richmond"}
# another way to iterate through the keys
#for key in capitals.keys():
#     print(key)
# output: Washington, California, Idaho, Illinois, Texas, Oklahoma, Virginia
#to iterate through the values
#for val in capitals.values():
#     print(val)
# output: Olympia, Sacramento, Boise, Springfield, Austin, Oklahoma City, Richmond
#to iterate through both keys and values
#for key, val in capitals.items():
#     print(key, " = ", val)
# output: Washington = Olympia, California = Sacramento, Idaho = Boise, etc

# List of dictionaries
#users = [
#    {"first": "Ada", "last": "Lovelace"}, # index 0
#    {"first": "Alan", "last": "Turing"}, # index 1
#    {"first": "Eric", "last": "Idle"} # index 2
#]
# Dictionary of lists
#resume_data = {
    #        	     0           1           2
#    "skills": ["front-end", "back-end", "database"],
    #                0           1
#    "languages": ["Python", "JavaScript"],
    #                0              1
#    "hobbies":["rock climbing", "knitting"]
#}

#considered a dictionary:
#kevin = {"name": "Kevin Durant", "age":34, "position": "small forward", "team": "Brooklyn Nets"}

#class Player: #class, ID
#    def __init__(self, name, age, position, team): #define initialization, values
#        self.name = name
#        self.age = age
#        self.position = position
#        self.team = team

# Pass in all the values from the dictionary by their keys
#player_kevin = Player(kevin["name"], kevin["age"], kevin["position"], kevin["team"])
#print(player_kevin.position) # prints small forward

# Encapsulation is the idea that we can group code together into objects; 
# hence Object Oriented Programming. We use classes or "coding blue prints" 
# to define what our objects are and how they behave. We encapsulate attributes 
# and methods in our class.
#class CoffeeM:
#    def __init__(self,name):
#        self.name = name
#        self.water_temp = 200
#    def brew_now(self,beans):
#        print(f"Using {beans}!")
#        print("Brew now brown cow!")
#    def clean(self):
#        print("Cleaning!")

# Inheritance is the idea that we pass along attributes and methods from one class 
# into a "sub-class" or child class, and not have to re-write the code to make it work.
# Child classes can be more specific versions of their Parent class.
# Using the key word "super" will call methods
#class CappuccinoM( CoffeeM ):
#    def __init__(self,name):
#        super().__init__(name)
#        self.milk = "whole"
#    def make_cappuccino(self,beans):
#        super().brew_now(beans)
#        print("Frothy!!!")

# Polymorphism means "many forms", and the idea in OOP is that a Child class can have a 
# different version of a method than the Parent class. In this example the child class of 
# CappuccinoM has a clean method, and so does CoffeeM. Depending on the class, the 
# clean method will do different things.
#class CappuccinoM( CoffeeM ):
#    def __init__(self,name):
#        super().__init__(name)
#        self.milk = "whole"
#    def make_cappuccino(self,beans):
#        super().brew_now(beans)
#        print("Frothy!!!")
#    def clean(self):
#        print("Cleaning the froth!")

# Abstraction is an extension of Encapsulation, and we can hide attributes or methods that 
# a Barista doesn't need to know about, like a CoffeeM. That way the Barista can make a cup 
# of coffee in a simpler manner.
#class Barista:
#    def __init__(self,name):
#        self.name = name
#        self.cafe = CoffeeM("Cafe")
#    def make_coffee(self):
#        self.cafe.brew_now()

#class Parent:
#    def method_a(self):
#        print("invoking Parent method_a!")
#class Child(Parent):
#    def method_a(self):
#        print("invoking Child method_a!")
#dad = Parent()
#son = Child()
#dad.method_a()
#son.method_a()

# We'll use the Person class to demonstrate polymorphism
# in which multiple classes inherit from the same class but behave in different ways
#class Person:
#  def pay_bill(self):
#      raise NotImplementedError
# Millionaire inherits from Person
#class Millionaire(Person):
#  def pay_bill(self):
#      print("Here you go! Keep the change!")
# Grad Student also inherits from the Person class
#class GradStudent(Person):
#  def pay_bill(self):
#      print("Can I owe you ten bucks or do the dishes?")

#favorite_color = input('What is your favorite color? ') 
# input takes a prompt, which needs to be a string
#print(f'Your favorite color is: {favorite_color}') 
#output, prints the color given to the console
