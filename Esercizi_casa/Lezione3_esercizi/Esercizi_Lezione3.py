# 4-1. Pizzas
pizzas: list[str] = ['margherita', 'marinara', 'diavola']
for pizza in pizzas:
    print(f"I like {pizza} pizza.")
print("I really love pizza!")

# 4-2. Animals
animals: list[str] = ['cat', 'dog', 'parrot']
for animal in animals:
    print(f"A {animal} would make a great pet.")
print("Any of these animals would make a great pet!")

# 4-3. Counting to Twenty
for number in range(1, 21):
    print(number)

# 4-4. One Million
# for number in range(1, 1000001):
#     print(number)

# 4-5. Summing a Million
numbers: list[int] = list(range(1, 1000001))
print(min(numbers))
print(max(numbers))
print(sum(numbers))

# 4-6. Odd Numbers
for number in range(1, 21, 2):
    print(number)

# 4-7. Threes
for number in range(3, 31, 3):
    print(number)

# 4-8. Cubes
cubes: list[int] = []
for number in range(1, 11):
    cube = number**3
    cubes.append(cube)
for cube in cubes:
    print(cube)

# 4-9. Cube Comprehension
cubes: list[int] = [number**3 for number in range(1, 11)]
for cube in cubes:
    print(cube)

# 4-10. Slices
print("The first three items in the list are:", cubes[:3])
print("Three items from the middle of the list are:", cubes[4:7])
print("The last three items in the list are:", cubes[-3:])

# 4-11. My Pizzas, Your Pizzas
friend_pizzas: list[str] = pizzas[:]
pizzas.append('capricciosa')
friend_pizzas.append('quattro formaggi')
print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)
print("My friend’s favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)

# 4-12. More Loops
fruits: list['str'] = ['apple', 'banana', 'orange', 'grape']
vegetables: list['str'] = ['salad', 'spinach', 'potato', 'carrot']
print("Fruits:")
for fruit in fruits:
    print(fruit)
print("\nVegetables:")
for vegetable in vegetables:
    print(vegetable)

# 5-1. Conditional Tests
car: str = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

# Additional tests
print("\nIs car == 'bmw'? I predict False.")
print(car == 'bmw')
print("\nIs car != 'bmw'? I predict True.")
print(car != 'bmw')
print("\nIs car == 'Subaru'? I predict False.")
print(car == 'Subaru')
print("\nIs car.lower() == 'subaru'? I predict True.")
print(car.lower() == 'subaru')

# 5-2. More Conditional Tests
number: int = 15
print("\nIs number == 15? I predict True.")
print(number == 15)
print("\nIs number != 15? I predict False.")
print(number != 15)
print("\nIs number > 10? I predict True.")
print(number > 10)
print("\nIs number < 10? I predict False.")
print(number < 10)
print("\nIs number >= 15? I predict True.")
print(number >= 15)
print("\nIs number <= 10? I predict False.")
print(number <= 10)

# List tests
numbers: list[int] = [1, 2, 3, 4, 5]
print("\nIs 3 in numbers? I predict True.")
print(3 in numbers)
print("\nIs 6 in numbers? I predict False.")
print(6 in numbers)

# 5-3. Alien Colors #1
alien_color: str = 'green'
if alien_color == 'green':
    print("\nThe alien's color is green. The player just earned 5 points.")

alien_color = 'red'
if alien_color == 'green':
    print("\nThe alien's color is green. The player just earned 5 points.")

# 5-4. Alien Colors #2
alien_color = 'green'
if alien_color == 'green':
    print("\nThe alien's color is green. The player just earned 5 points.")
else:
    print("\nThe alien's color isn't green. The player just earned 10 points.")

alien_color = 'red'
if alien_color == 'green':
    print("\nThe alien's color is green. The player just earned 5 points.")
else:
    print("\nThe alien's color isn't green. The player just earned 10 points.")

# 5-5. Alien Colors #3
alien_color: str = 'green'
if alien_color == 'green':
    print("\nThe alien's color is green. The player earned 5 points.")
elif alien_color == 'yellow':
    print("\nThe alien's color is yellow. The player earned 10 points.")
else:
    print("\nThe alien's color is red. The player earned 15 points.")

alien_color: str = 'yellow'
if alien_color == 'green':
    print("\nThe alien's color is green. The player earned 5 points.")
elif alien_color == 'yellow':
    print("\nThe alien's color is yellow. The player earned 10 points.")
else:
    print("\nThe alien's color is red. The player earned 15 points.")

alien_color: str = 'red'
if alien_color == 'green':
    print("\nThe alien's color is green. The player earned 5 points.")
elif alien_color == 'yellow':
    print("\nThe alien's color is yellow. The player earned 10 points.")
else:
    print("\nThe alien's color is red. The player earned 15 points.")

# 5-6. Stages of Life
age: int = 25
if age < 2:
    print("\nThe person is a baby.")
elif age < 4:
    print("\nThe person is a toddler.")
elif age < 13:
    print("\nThe person is a kid.")
elif age < 20:
    print("\nThe person is a teenager.")
elif age < 65:
    print("\nThe person is an adult.")
else:
    print("\nThe person is an elder.")

# 5-7. Favorite Fruit
favorite_fruits: list[str] = ['apple', 'banana', 'orange']
if 'apple' in favorite_fruits:
    print("\nYou really like apples!")
if 'banana' in favorite_fruits:
    print("\nYou really like bananas!")
if 'orange' in favorite_fruits:
    print("\nYou really like oranges!")
if 'mango' in favorite_fruits:
    print("\nYou really like mangoes!")
if 'strawberry' in favorite_fruits:
    print("\nYou really like strawberries!")

# 5-8. Hello Admin
usernames: list[str] = ['admin', 'user1', 'user2', 'user3', 'user4']
for username in usernames:
    if username == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {username}, thank you for logging in again.")

# 5-9. No Users
usernames: list[str] = []
if usernames:
    for username in usernames:
        print(f"Hello {username}, thank you for logging in again.")
else:
    print("We need to find some users!")

# 5-10. Checking Usernames
current_users: list[str] = ['admin', 'user1', 'user2', 'user3', 'user4']
new_users: list[str] = ['user5', 'user6', 'admin', 'user7', 'user8']
current_users_lower: list[str] = [user.lower() for user in current_users]
for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"Username {new_user} is already used, you will need to enter a new username.")
    else:
        print(f"Username {new_user} is available.")

# 5-11. Ordinal Numbers
numbers: list[int] = list(range(1,10))
for number in numbers:
    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print("3rd")
    else:
        print(f"{number}th")
