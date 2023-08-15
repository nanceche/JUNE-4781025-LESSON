from statistics import mean
class Student:
    def __init__(self,namevar,agevar,classver="General"):
        self.age = agevar
        self.name = namevar
        self.classroom = classver 

    def grades(self,maths,english,science):
        self.maths= maths 
        self.english = english 
        self.science= science 

        return mean([self.maths,self.english,self.science])





Serena = Student("Serena", 24, "History")
Serena_grades=Serena.grades(20,17,19)
Venus = Student("Venus", 28)

print(Serena.age)

print(Serena_grades)

