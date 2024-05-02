# 8-1. Message
def display_message() -> None:
    print("I am learning about functions in this chapter.")

display_message()

# 8-2. Favorite Book
def favorite_book(title: str) -> None:
    print(f"One of my favorite books is {title}.")

favorite_book("Alice in Wonderland")

# 8-3. T-Shirt
def make_shirt(size: str, message: str) -> None:
    print(f"The size of the shirt is {size} and the message printed on it is '{message}'.")

make_shirt('M', 'Hello World')
make_shirt(size='L', message='Python Rocks')

# 8-4. Large Shirts
def make_shirt(size: str = 'L', message: str = 'I love Python') -> None:
    print(f"The size of the shirt is {size} and the message printed on it is '{message}'.")

make_shirt()
make_shirt(size='M')
make_shirt(message='Hello World')

# 8-5. Cities
def describe_city(city: str, country: str = 'Italy') -> None:
    print(f"{city} is in {country}.")

describe_city('Milan')
describe_city('Paris', 'France')
describe_city('Berlin', 'Germany')

# 8-6. City Names
def city_country(city: str, country: str) -> str:
    return f"{city}, {country}"

print(city_country('Santiago', 'Chile'))
print(city_country('Madrid', 'Spain'))
print(city_country('Rome', 'Italy'))

# 8-7. Album
def make_album(artist: str, title: str, songs: int = None) -> dict[str, str | int]: 
    album = {'artist': artist, 'title': title}
    if songs:
        album['songs'] = songs
    return album

album1: dict[str, str | int] = make_album('The Beatles', 'Abbey Road') 
album2: dict[str, str | int] = make_album('Pink Floyd', 'The Wall') 
album3: dict[str, str | int] = make_album('Vasco Rossi', 'Vita spericolata', 8) 

print(f"Album 1: {album1}")
print(f"Album 2: {album2}")
print(f"Album 3: {album3}")

# 8-8. User Albums
while True:
    artist = input("Enter the artist's name (or 'q' to quit): ")
    if artist == 'q':
        break
    title = input("Enter the album title: ")
    print(make_album(artist, title))

# 8-9. Messages
def show_messages(messages: list[str]) -> None:
    for message in messages:
        print(message)

messages = ['Hello', 'How are you?', 'Goodbye']
show_messages(messages)

# 8-10. Sending Messages
def send_messages(messages: list[str], sent_messages: list[str]) -> None:
    while messages:
        message = messages.pop()
        print(message)
        sent_messages.append(message)

messages = ['Hello', 'How are you?', 'Goodbye']
sent_messages = []
send_messages(messages, sent_messages)
print(messages)
print(sent_messages)

# 8-11. Archived Messages
messages = ['Hello', 'How are you?', 'Goodbye']
sent_messages = []
send_messages(messages[:], sent_messages)
print(messages)
print(sent_messages)

# 8-12. Sandwiches
def make_sandwich(items: list[str]) -> None:
    print("Making a sandwich with the following items:")
    for item in items:
        print(f"- {item}")

make_sandwich(['ham', 'cheese', 'tomato'])
make_sandwich(['chicken', 'lettuce'])
make_sandwich(['olive oil', 'jelly'])

# 8-13. User Profile
def build_profile(first: str, last: str, age: int, hair: str, weight: int) -> str:
    user_info: dict[str, str | int] = {}
    user_info['first_name'] = first
    user_info['last_name'] = last
    user_info['age'] = age
    user_info['hair'] = hair
    user_info['weight'] = weight
    return ', '.join([f"{k}: {v}" for k, v in user_info.items()])

print(build_profile('Eric', 'Crow', 45, 'brown', 67))

# 8-14. Cars
def make_car(manufacturer: str, model: str, color: str = None, tow_package: bool = None) -> dict[str, str | bool]:
    car: dict[str, str | bool] = {}
    car['manufacturer'] = manufacturer
    car['model'] = model
    if color:
        car['color'] = color
    if tow_package is not None:
        car['tow_package'] = tow_package
    return car

car: dict[str, str | bool] = make_car('subaru', 'outback', color='blue', tow_package=True)
print(f"Car: {car}")

# 8-16. Imports
import make_sandwich_function
from make_sandwich_function import make_sandwich
from make_sandwich_function import make_sandwich as fn
import make_sandwich_function as mn
from make_sandwich_function import *
