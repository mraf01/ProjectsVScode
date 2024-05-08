class Animal:
    def __init__(self, name, legs):
        self.name = name
        self.legs = legs

    def setLegs(self, legs):
        self.legs = legs

    def getLegs(self):
        return self.legs

    def printInfo(self):
        print(f"Name: {self.name}, Legs: {self.legs}")

# 1
dog = Animal("Dog", 4)
cat = Animal("Cat", 4)

# 2
print(dog.name)
print(cat.name)

# 3
dog.legs = 3
print(dog.legs)

# 4
cat.setLegs(3)
print(cat.getLegs())

# 5
print(dog.getLegs())
print(cat.getLegs())

# 6
dog.printInfo()
cat.printInfo()
