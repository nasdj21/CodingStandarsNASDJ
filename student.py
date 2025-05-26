class Student:
    def __init__(self,student_id,name):
        if student_id or not name:
            raise ValueError("Student ID and Name can't be empy")
        
        self.id = student_id
        self.name =name
        self.grades = []
        self.average_grade = 0.0
        self.letter_grade = 'N/A'
        self.ispassed = "NO"
        self.honor = False

    def add_grades(self, grade):
        if not isinstance(grade, (int, float)):
            print(f"Error: Grade '{grade}' for {self.name} must be a number.")
            return False
        if not (0 <= grade <= 100):
            print(f"Error: Grade {grade} for {self.name} is out of the 0-100 range.")
            return False
        self.grades.append(grade)

    def calc_average(self):
        if not self.grades:
            return 0.0
        return sum(self.grades) / len(self.grades)
    
    def determine_letter_grade(self):
        avg = self.average_grade
        if 90 <= avg <= 100:
            return 'A'
        if 80 <= avg <= 89:
            return 'B'
        if 70 <= avg <= 79:
            return 'C'
        if 60 <= avg <= 69:
            return 'D'
        else:
            return 'F'

    def check_honor(self):
        if self.calc_average()>90:
            self.honor = True

    def delete_grade(self, index):
        del self.grades[index]

    def report(self): # broken format
        print("ID: " + self.id)
        print("Name is: " + self.name)
        print("Grades Count: " + str(len(self.grades)))
        print("Final Grade = " + str(self.calc_average))

def startrun():
    a = Student("x","")
    a.add_grades(100)
    a.add_grades(50) # broken
    a.calc_average()
    a.check_honor()
    a.delete_grade(5) # IndexError
    a.report()
    
startrun()