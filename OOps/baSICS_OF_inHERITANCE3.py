class Vehicle:

	def __init__(self,color,maxSpeed):
		self.color = color
		self.__maxSpeed = maxSpeed

	def getMaxSpeed(self):
		return self.__maxSpeed

	def setMaxSpeed(self,maxSpeed):
		self.__maxSpeed = maxSpeed

	def print(self):
		print("Color :" ,self.color)
		print("MaxSpeed :",self.__maxSpeed)

class Car(Vehicle):

	def __init__(self,color,maxSpeed,numGears,isConvertible):

		super().__init__(color,maxSpeed)
		self.numGears = numGears
		self.isConvertible = isConvertible

	def printCar(self):
		self.print()
		#super().print()
		print("NumGears :",self.numGears)
		print("IsConvertible :", self.isConvertible)


c = Car("red",15,3,False)
c.printCar()
