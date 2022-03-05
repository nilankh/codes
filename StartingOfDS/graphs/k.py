##class Square:
##    def __init__(self, side):
##        self.side = side
##    def area(self):
##        return self.side ** 2
##
##class Cube(Square):
##    def surface_area(self):
##        area = super().area()
##        return 6 * area
##
####print(Cube().surface_area(6))
####print(Square.Cube(6).surface_area())
####print(Cube(6).surface_area())
##print(Square.Cube().surface_area(6))
item_1 = "bread"
item_2 = "milk"
item_3 = "cheese"
greeting = "I need " + item_1 + ", " + item_2 + ", and " + item_3 + "."
print(greeting)

##values = ["I need", "bread", "milk", "and", "cheese"]
##greeting = " ".join(values)
##print(greeting)
