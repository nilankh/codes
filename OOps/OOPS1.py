class Student:
    passingPercentage=40
    def studentDetails(self):
        self.name="Parikh"
        print("Name=",self.name)
        self.percentage=80
        print("Percentage = ",self.percentage)
        pass
    def isPassed(self):
        if self.percentage>Student.passingPercentage:
            print("Student is passed")
        else:
            print("Student is not paseed")
    @staticmethod #this is called as decorator
    def welcomeToSchool():
        print("Hey! welcome to school")
s1=Student()
s1.studentDetails()
Student.studentDetails(s1)
s1.isPassed()
s1.welcomeToSchool()