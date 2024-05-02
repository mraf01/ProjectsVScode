# 2-3. Personal Message
name: str = "Eric"
print(f"Hello {name}, would you like to learn some Python today?")

# 2-4. Name Cases
name: str = "Eric"
print(name.lower())
print(name.upper())
print(name.title())

# 2-5. Famous Quote
print('Albert Einstein once said, "A person who never made a mistake never tried anything new."')

# 2-6. Famous Quote 2
famous_person: str = "Albert Einstein"
message: str = f'{famous_person} once said, "A person who never made a mistake never tried anything new."'
print(message)

# 2-8. File Extensions
filename: str = 'python_notes.txt'
print(filename.removesuffix('.txt'))

# 3-1. Names
names: list[str] = ["Luca", "Alice", "Fabio"]
for name in names:
    print(name)

# 3-2. Greetings
for name in names:
    print(f"Hello {name}, how are you today?")

# 3-3. Your Own List
vehicles: list[str] = ["Honda motorcycle", "Tesla car", "Ferrari"]
for vehicle in vehicles:
    print(f"I would like to own a {vehicle}.")

# 3-4. Guest List
guests: list[str] = ["Luca", "Alice", "Fabio"]
for guest in guests:
    print(f"Hello {guest}, I would like to invite you to dinner.")

# 3-5. Changing Guest List
print(f"{guests[0]} can't make it to the dinner.")
guests[0] = "Davide"
for guest in guests:
    print(f"Hello {guest}, I would like to invite you to dinner.")

# 3-6. More Guests
print("I found a bigger table.")
guests.insert(0, "Matteo")
guests.insert(len(guests)//2, "Francesco")
guests.append("Gabriele")
for guest in guests:
    print(f"Hello {guest}, I would like to invite you to dinner.")

# 3-7. Shrinking Guest List
print("I can invite only two people for dinner.")
while len(guests) > 2:
    removed_guest: str = guests.pop()
    print(f"Sorry {removed_guest}, I can't invite you to dinner.")
for guest in guests:
    print(f"Hello {guest}, you're still invited.")
del guests[:]
print(guests)

# 3-8. Seeing the World
places: list[str] = ["Rome", "Tokyo", "New York", "London", "Paris"]
print(places)
print(sorted(places))
print(places)
print(sorted(places, reverse=True))
print(places)
places.reverse()
print(places)
places.reverse()
print(places)
places.sort()
print(places)
places.sort(reverse=True)
print(places)

# 3-9. Dinner Guests
guests: list[str] = ["Luca", "Alice", "Fabio"]
print(f"I'm inviting {len(guests)} people to dinner.")

# 3-10. Every Function
items: list[str] = ["Mount Everest", "Amazon River", "Italy", "Rome", "English"]
print(items)
print(len(items))
items.append("French")
print(items)
items.insert(0, "K2")
print(items)
del items[0]
print(items)
popped_item: str = items.pop()
print(popped_item)
print(items)
items.remove("Italy")
print(items)

# 6-1. Person
person: dict[str, str | int] = {"first_name": "Mario", "last_name": "Rossi", "age": 30, "city": "Rome"}
for key, value in person.items():
    print(f"{key}: {value}")

# 6-2. Favorite Numbers
favorite_numbers: dict[str, int] = {"Luca": 10, "Alice": 7, "Fabio": 50, "Davide": 9, "Mario": 2}
for name, number in favorite_numbers.items():
    print(f"{name}'s favorite number is {number}.")

# 6-3. Glossary
glossary: dict[str, str] = {
    "string": "A series of characters.",
    "variable": "A reserved memory location to store values.",
    "dictionary": "A collection of key-value pairs.",
    "function": "A named block of code designed to do a specific job.",
    "loop": "Work through a collection of items, one at a time.",
}
for word, definition in glossary.items():
    print(f"\n{word}:")
    print(f"  {definition}")

# 6-7. People
people: list[dict[str, str | int]] = []
people.append(person)
people.append({
    "first_name": "Matteo",
    "last_name": "Bianchi",
    "age": 25,
    "city": "Milan",
})
people.append({
    "first_name": "Chiara",
    "last_name": "Marrone",
    "age": 35,
    "city": "Naples",
})
for person in people:
    for key, value in person.items():
        print(f"{key}: {value}")
    print()

# 6-8. Pets
pets: list[dict[str, str]] = []
pets.append({"animal": "cat", "owner": "Fabio"})
pets.append({"animal": "dog", "owner": "Davide"})
pets.append({"animal": "bird", "owner": "Chiara"})
for pet in pets:
    for key, value in pet.items():
        print(f"{key}: {value}")
    print()

# 6-9. Favorite Places
favorite_places: dict[str, list[str]] = {
    "Matteo": ["Milan", "Madrid"],
    "Luca": ["Tokyo"],
    "Alice": ["Rome", "Paris", "New York"],
}
for name, places in favorite_places.items():
    print(f"\n{name}'s favorite places are:")
    for place in places:
        print(f"  {place}")

# 6-10. Favorite Numbers
favorite_numbers: dict[str, list[int]] = {
    "Matteo": [3, 8],
    "Luca": [7, 6],
    "Davide": [1, 0],
    "Mario": [9, 5],
    "Chiara": [2, 4],
}
for name, numbers in favorite_numbers.items():
    print(f"\n{name}'s favorite numbers are:")
    for number in numbers:
        print(f"  {number}")

# 6-11. Cities
cities: dict[str, dict[str, str | int]] = {
    "Rome": {
        "country": "Italy",
        "population": 2873000,
        "fact": "Rome is the capital of Italy with a history that goes back over 2,500 years.",
    },
    "New York": {
        "country": "USA",
        "population": 8623000,
        "fact": "It's known as 'The City That Never Sleeps'.",
    },
    "London": {
        "country": "UK",
        "population": 8900000,
        "fact": "London is the biggest city in western Europe, and the world's largest financial centre.",
    },
}
for city, info in cities.items():
    print(f"\n{city}:")
    for key, value in info.items():
        print(f"  {key}: {value}")

# 6-12. Extensions
cities["Rome"]["language"] = "Italian"
cities["Rome"]["landmark"] = "Colosseum"
cities["New York"]["language"] = "English"
cities["New York"]["landmark"] = "Statue of Liberty"
cities["London"]["language"] = "English"
cities["London"]["landmark"] = "Big Ben"
for city, info in cities.items():
    print(f"\n{city}:")
    for key, value in info.items():
        print(f"  {key}: {value}")        
