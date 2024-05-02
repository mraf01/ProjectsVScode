# 8-16. Imports

def make_sandwich(items: list[str]) -> None:
    print("Making a sandwich with the following items:")
    for item in items:
        print(f"- {item}")

make_sandwich(['ham', 'cheese', 'tomato'])
make_sandwich(['chicken', 'lettuce'])
make_sandwich(['olive oil', 'jelly'])
