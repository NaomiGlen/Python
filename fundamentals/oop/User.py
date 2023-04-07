class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

    def display_info(self):
        print("========================")
        print(f"First name: {self.first_name}")
        print(f"Last name: {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age}")
        print(f"Member: {self.is_rewards_member}")
        print(f"Current Points: {self.gold_card_points}")
        print("========================")
        return self

    def enroll(self):
        if self.is_rewards_member == True:
            print("User is already a member")
        else:
            self.is_rewards_member = True
            self.gold_card_points = 200
        return self

    def spend_points(self, amount):
        if amount < self.gold_card_points:
            self.gold_card_points -= amount
        else:
            print("Sorry, you do not have enough points.")
        return self

naomi = User("Naomi", "Glen", "naomi@email.com", 43)
ginger = User("Ginger", "Davis", "ginger@email.com", 41)
overspender = User("Over", "Spender", "overspender@email.com", 20)
cool_user = User("Adonis", "Creed", "acreed@email.com", 27)

naomi.enroll().spend_points(50).display_info()

ginger.enroll().spend_points(80).display_info()

overspender.display_info().spend_points(40)

cool_user.enroll().display_info()

naomi.enroll()