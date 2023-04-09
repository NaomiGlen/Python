class Pet:
    def __init__(self, name, type, tricks, noise):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 200
        self.energy = 100
        self.noise = noise
    def sleep(self):
        self.energy += 25
        return self
    def eat(self):
        self.energy += 5
        self.health += 10
        return self
    def play(self):
        self.health += 5
        return self
    def noise(self):
        print(self.noise)

class Ninja:
    def __init__(self, f_name, l_name, pet, treats, pet_food):
        self.f_name = f_name
        self.l_name = l_name
        self.pet = pet
        self.treats = treats
        self.pet_food = pet_food
    def walk(self):
        self.pet.play()
        return self
    def give_treat(self):
        if len(self.treats) >0:
            treat = self.treats.pop()
            print(f"Giving {self.pet.name} a {treat}!")
            self.pet.eat()
        else:
            print("Oh shoot! You're out of treats!")
        return self
    def feed(self):
        if len(self.pet_food) >0:
            food = self.pet_food.pop()
            print(f"Feeding {self.pet.name} {food}!")
            self.pet.eat()
        else:
            print("Oh no!! You need more pet food!")
        return self
    def bathe(self):
        self.pet.noise()

treats = ['Ferret Chew Stick', 'Marshall Peanut Butter Bandits', 'Freeze-Dried Raw Chicken Heart']
pet_food = ['Epigen 90', 'Marshall Premium Ferret Food']

tanjiro = Pet("Tanjiro", "Ferret", ['slides through tubes', 'plays with toys', 'naps on shoulder'], "Squeek!")
naomi = Ninja("Naomi", "Glen", tanjiro, treats, pet_food)

naomi.walk();
naomi.feed();
naomi.walk();
naomi.walk();
naomi.give_treat();
naomi.give_treat();
naomi.give_treat();
naomi.give_treat();
naomi.walk();
naomi.feed();
naomi.feed();
naomi.bathe();