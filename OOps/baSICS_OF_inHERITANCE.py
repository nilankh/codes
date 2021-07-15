class Vehicle:
    def __init__(self,color,maxSpeed):
        self.color=color
        self.maxSpeed=maxSpeed

class Car(Vehicle):
    def __init__(self,color,maxSpeed,numGears,isConvertible):

        super().__init__(color,maxSpeed)
        self.numGears=numGears
        self.isConvertible=isConvertible

    def printCar(self):
        print("Color : ",self.color)
        print("MaxSpeed : ",self.maxSpeed)
        print("numGears : ",self.numGears)
        print("IsConvertible : ",self.isConvertible)

c=Car("Red",180,5,False)
c.printCar()
