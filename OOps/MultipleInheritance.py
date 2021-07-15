'''
class Mother:
    def print(self):
        print("print of mother called")
class Father:
    def print(self):
        print("Print of father called")
class child(Father,Mother):#the order we have defined father & mother that will workm first
    def __init__(self,name):
        self.name=name
    def printChild(self):
        print("NAME OF CHILD IS",self.name)

c=child("ROHAN")
c.printChild()
c.print()
'''
#another example

class Mother:
    def __init__(self):
        self.name="Manju"
    def print(self):
        print("print of mother called")
class Father:
    def __init__(self):
        self.name="Ajay"
    def print(self):
        print("Print of father called")
class child(Mother,Father):#the order we have defined father & mother that will workm first
    def __init__(self):
        super().__init__()
    def printChild(self):
        print("NAME OF CHILD IS",self.name)

c=child()
c.printChild()
#c.print()
