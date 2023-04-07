# declare a class and give it name User
class User:		
    def __init__(self):
        self.first_name = "Ada"
        self.last_name = "Lovelace"
        self.age = 42

    def greeting(self):
        print(f"Hello, my name is {self.first_name}")

user_ada = User() #create a variable for the class
print(user_ada.first_name) #runs print function of variable and class sub-variable
print(user_ada.last_name) #runs print function of variable and class sub-variable

user_2 = User() #Creates a second id with same info as first but with a different variable
print(user_2.last_name) #runs print function of variable and class sub-variable

print(user_ada) #prints object id because it's not asking for any specific information