class Student:
    def __init__(self, name, studyProgram, age, gender):
        self.name = name
        self.studyProgram = studyProgram
        self.age = age
        self.gender = gender

    def printInfo(self):
        print(f"Name: {self.name}, Study Program: {self.studyProgram}, Age: {self.age}, Gender: {self.gender}")

me = Student("Matteo", "Cloud", 23, "M")
left_neighbour = Student("Davide", "Cloud", 18, "M")
right_neighbour = Student("Lorenzo", "Cloud", 19, "M")

me.printInfo()
left_neighbour.printInfo()
right_neighbour.printInfo()