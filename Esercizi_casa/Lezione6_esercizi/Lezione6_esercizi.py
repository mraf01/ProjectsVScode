# 9-1. Restaurant

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Welcome to {self.restaurant_name}! We serve {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")

restaurant = Restaurant("McDonald's", "American")

print(f"Restaurant Name: {restaurant.restaurant_name}")
print(f"Cuisine Type: {restaurant.cuisine_type}")

restaurant.describe_restaurant()
restaurant.open_restaurant()

# 9-2. Three Restaurants

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"The name of the restaurant is {self.restaurant_name} and it serves {self.cuisine_type} cuisine.")

restaurant1 = Restaurant("Chinese Food", "Hot Noodles")
restaurant2 = Restaurant("McDonald's", "Big Mac")
restaurant3 = Restaurant("Japanese Food", "Sushi")

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()

# 9-3. Users

class User:
    def __init__(self, first_name, last_name, age, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email

    def describe_user(self):
        print(f"User: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Email: {self.email}")

    def greet_user(self):
        print(f"Hello, {self.first_name}! Welcome back.")

user1 = User("Mario", "Rossi", 30, "mario@example.com")
user2 = User("Alice", "Verdi", 25, "alice@example.com")

user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

# 9-4. Number Served

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"Welcome to {self.restaurant_name}! We serve {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")

    def set_number_served(self, num_customers):
        self.number_served = num_customers

    def increment_number_served(self, additional_customers):
        self.number_served += additional_customers

restaurant = Restaurant("McDonald's", "American")

print(f"Initial Number of Customers Served: {restaurant.number_served}")

restaurant.set_number_served(50)
print(f"Updated Number of Customers Served: {restaurant.number_served}")

restaurant.increment_number_served(20)
print(f"New Total Number of Customers Served: {restaurant.number_served}")

# 9-5. Login Attempts

class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

user = User("Fabio", "Mario")

user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()

print(f"Login Attempts: {user.login_attempts}")

user.reset_login_attempts()
print(f"Login Attempts after reset: {user.login_attempts}")

# 9-6. Ice Cream Stand

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []

    def display_flavors(self):
        print(f"Ice cream flavors available at {self.restaurant_name}:")
        for flavor in self.flavors:
            print(f"- {flavor}")

ice_cream_stand = IceCreamStand("Ice Cream Shop" "Ice Cream")
ice_cream_stand.flavors = ["Vanilla", "Chocolate", "Strawberry"]

ice_cream_stand.display_flavors()

# 9-7. Admin

class Admin(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = []

    def show_privileges(self):
        if self.privileges:
            print("Administrator privileges:")
            for privilege in self.privileges:
                print(f"- {privilege}")
        else:
            print("No privileges set for this admin")

admin = Admin("Admin", "Mario")
admin.privileges = ["can add post", "can delete post", "can ban user"]

admin.show_privileges()

# 9-8. Privileges

class Privileges:
    def __init__(self):
        self.privileges = []

    def show_privileges(self):
        if self.privileges:
            print("Privileges:")
            for privilege in self.privileges:
                print(f"- {privilege}")
        else:
            print("No privileges set")

admin.privileges = Privileges()
admin.privileges.privileges = ["can edit user profiles", "can moderate comments"]

admin.show_privileges()

# 9-13. Dice

import random

class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        return random.randint(1, self.sides)

six_sided_die = Die()
print("Rolling a 6-sided die 10 times:")
for _ in range(10):
    print(six_sided_die.roll_die())

ten_sided_die = Die(sides=10)
print("\nRolling a 10-sided die 10 times:")
for _ in range(10):
    print(ten_sided_die.roll_die())

twenty_sided_die = Die(sides=20)
print("\nRolling a 20-sided die 10 times:")
for _ in range(10):
    print(twenty_sided_die.roll_die())

# 9-14. Lottery

import random

def generate_lucky_numbers():
    return [random.randint(1, 100) for _ in range(5)]

def main():
    print("Welcome to Lucky Lottery Numbers!")
    user_numbers = input("Enter 5 numbers (separated by spaces): ").split()

    user_numbers = [int(num) for num in user_numbers]
    lucky_numbers = generate_lucky_numbers()
    common_numbers = set(user_numbers) & set(lucky_numbers)
    
    print("\nYour selected numbers:", user_numbers)
    print("Lucky lottery numbers:", lucky_numbers)

    if common_numbers:
        print(f"\nCongratulations! You matched {len(common_numbers)} number(s): {common_numbers}")
    else:
        print("\nBetter luck next time!")

if __name__ == "__main__":
    main()

# 9-15. Lottery Analysis

import random

def generate_ticket():
    my_ticket = random.sample(range(1, 11), 4)
    return my_ticket

def simulate_lottery():
    return random.sample(range(1, 11), 4)

def main():
    winning_ticket = generate_ticket()
    num_simulations = 0

    while True:
        num_simulations += 1
        if simulate_lottery() == winning_ticket:
            break

    print(f"Congratulations! You won after {num_simulations} tries.")
    print(f"Your winning ticket: {winning_ticket}")

if __name__ == "__main__":
    main()