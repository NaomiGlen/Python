# class User:

#     def __init__(self,f_name, l_name, age):
#         self.first_name = f_name
#         self.last_name = l_name
#         self.age = age

#     def introduce(self):
#         print(f'Hello my name is {self.first_name} {self.last_name}')

#     def change_first_name(self, new_name):
#         self.first_name = new_name

#     def birthday(self):
#         self.age += 1
#         print(self.age)




# kyle = User("Kyle", "Reimers", 28)
# print(kyle)

# Trae= User("Trae", "hughes", 24)

# # kyle.introduce()
# # kyle.change_first_name("Billy")
# # kyle.introduce()
# # kyle.birthday()
# # Trae.introduce()








class Car:


    def __init__(self, make, model, year, color, mileage):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.mileage = mileage


    def drive(self):
        self.mileage += 20
        print("vroom vroom")


car1 = Car("Hummer", "H2", 2005, "Yellow", 5000)


car1.drive()
print(car1.mileage)
# print(car1.make)