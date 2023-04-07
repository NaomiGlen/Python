class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
    def greeting(self):
        print(f"Hello, my name is {self.name}")

naomi = User("Naomi", "naomi@email.com")
cool_person = User("Adrien", "adion@codingdojo.com")

naomi.greeting()
cool_person.greeting()