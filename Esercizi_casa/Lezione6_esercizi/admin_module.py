# 9-11. Imported Admin

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

class Admin(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = Privileges()

# 9-12. Multiple Modules

from user_module import User
from privileges_module import Privileges

class Admin(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = Privileges()