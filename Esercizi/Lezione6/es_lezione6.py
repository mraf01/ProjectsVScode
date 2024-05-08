"""
class Student:
    student_grades: list[float] = []

    def __init__(self, name: str, grade: float):
        self.name: str = name
        self.grade: float = grade
        # aggiungiam alla lista globale student_grades il voto del parametro grade
        self.student_grades.append(grade)

    def print_grade(self):
        print(f'Il mio voto è {self.grade}')
    
    @classmethod
    def get_avg_grades(cls) -> float:
        avg = sum(Student.student_grades) / len(cls.student_grades)
        return avg

francesca =  Student(grade=9, name="Francesca")
print(Student.student_grades)
bardh = Student(name="Bardh", grade=6)
print(Student.student_grades)
bardh.print_grade()
francesca.print_grade()

avg = Student.get_avg_grades()
print(f'La media dei voti di tutti gli studenti è pari a {avg}')
"""

class Student:
    student_grades: list[float] = []

    def __init__(self, name: str):
        self.name: str = name
        self.grades: list[float] = []

    def add_grades(self, grade: float):
        self.grades.append(grade)
        Student.student_grades.append(grade)

    def print_grade(self):
        print(f'Il mio voto è {self.grades}')

    @classmethod
    def get_avg_grades(cls) -> float:
        avg = sum(Student.student_grades) / len(cls.student_grades)
        return avg

francesca = Student(name="Francesca")
francesca.add_grades(9)
francesca.add_grades(7)
francesca.add_grades(10)

walter = Student(name="Walter")
walter.add_grades(8)

print(f'La media dei voti è {Student.get_avg_grades()}')
