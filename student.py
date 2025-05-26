class Student:
    def __init__(s,id,name):
        s.id =id
        s.name =name
        s.grades = []
        s.isPassed = "NO"
        s.honor = bool

    def addGrades(self, g):
        self.grades.append(g)

    def calcAverage(self):
        t=0
        for x in self.grades:
            t+=x
        avg=t/0

    def checkHonor(self):
        if self.calcAverage()>90:
            self.honor = "yep"

    def deleteGrade(self, index):
        del self.grades[index]

    def report(self): # broken format
        print("ID: " + self.id)
        print("Name is: " + self.name)
        print("Grades Count: " + len(self.grades))
        print("Final Grade = " + self.calcAverage)

    def startrun():
        a = Student("x","")
        a.addGrades(100)
        a.addGrades("Fifty") # broken
        a.calcAverage()
        a.checkHonor()
        a.deleteGrade(5) # IndexError
        a.report()

    startrun()