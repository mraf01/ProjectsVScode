class Person:
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Height: {self.height}cm, Weight: {self.weight}kg"

alice = Person("Alice W.", 45, 165, 70)
bob = Person("Bob M.", 36, 175, 80)

# 1. Print the age of Bob
print(bob.age)

# 2. Print the name of the oldest person
if alice.age > bob.age:
    print(alice.name)
else:
    print(bob.name)

# 3. Create three more Persons and add all to a list
matteo = Person("Matteo C.", 50, 180, 85)
davide = Person("Davide M.", 40, 170, 75)
luca = Person("Luca R.", 30, 160, 65)

people = [alice, bob, matteo, davide, luca]

# 4. Find and print the youngest person's name
youngest = people[0]
for person in people:
    if person.age < youngest.age:
        youngest = person

print(youngest.name)

""" 
youngest = people[0]
for i in range(1, len(people)):
    if people[i].age < youngest.age:
        youngest = people[i]
print(youngest.name) 
"""

"""
youngest = people[0]
for i, person in enumerate(people):
    if i == 0:
        continue
    if person.age < youngest.age:
        youngest = person
print(youngest.name)
"""

"""
min_age = float('inf')
index_min_age = 0
for i in range(len(people)):
    if people[i].age < min_age:
        min_age = people[i].age
        index_min_age = i
print(people[index_min_age].name)
"""

# Print the details of each person
for person in people:
    print(person)