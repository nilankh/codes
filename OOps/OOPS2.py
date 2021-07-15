
class Student:
    def __init__(self,name,rollNumber):
        self .name=name
        self.rollNumber=rollNumber
s1=Student("NILANK NIKHIL",39)
print(s1.__dict__)

#belows these are mcq
'''
class Student:
    def __init__(self,name,age):
            self.name = "Rohan"
            self.age = 20
    def print_student_details():
            print(self.name, end= " ")
            print(self.age)


s = Student()
s.print_student_details()
'''

'''
class Student:
    def __init__(self,name,age):
        self.name = "Rohan"
        self.age = 20

    def print_student_details():
        print(self.name, end= " ")
        print(self.age)
s = Student("Parikh",25)
s.print_student_details()'''

'''
class Student:
     def __init__(self,name,age):
        self.__name = name
        self.age = age
     def print_student_details(self):
        print(self.__name, end= " ")
        print(self.age)
s = Student("Rohan",20)
s.print_student_details()'''
