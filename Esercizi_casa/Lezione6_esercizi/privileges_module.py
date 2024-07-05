# 9-12. Multiple Modules

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