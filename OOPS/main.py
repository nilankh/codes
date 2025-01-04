# class Item:
#     # need of self, python passes the object itself as a first argument, when you go ahead and call those methods. Now, if i item1.calculate_total_price() is called, python will pass item1 as a first argument to calculate_total_price method.
#     def  calculate_total_price(self, price, quantity):
#         return price * quantity

# item1 = Item()
# item1.name = "phone"
# item1.price = 100
# item1.quantity = 5
# print(item1.calculate_total_price(item1.price, item1.quantity))
# # print(type(item1))
# # print(type(item1.name))
# # print(type(item1.price))
# # print(type(item1.quantity))

# item1 = Item()
# item1.name = "Laptop"
# item1.price = 1000
# item1.quantity = 3
# print(item1.calculate_total_price(item1.price, item1.quantity))

"""
    the problem in above code is we don't have a set of rules for the attributes that you would like to pass in order to instantiate successfully. It means, that for each item that i need to go ahead and create, I need to hard code iin the attribute name, it will be nicers if we call somehow declaring the class that in order to instantiate an instance successfully, name, price and quantity are required.

"""

class Item:
    # what does this method do? It is called when you create an instance of the class. Python executes this double undescore init function automatically. it means, item1 = Item() first isme khud ko hi refere krta hai, self is the object itself.
    # def __init__(self, name, price,quantity=0):
    def __init__(self, name: str, price: float,quantity=0):
        # suppose i dont want to receive the negative values for quantity & price
        # assert statements, is a keyword that is used to check if there is a match between what is happening to your expecations
        # run valudations to the received values
        assert price >= 0, f"Price {price} is not valid"
        assert quantity >= 0, f"Quantity {quantity} is not valid"

        # these all are instance attributes, they are associated with the instance of the class
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity
    

item1 = Item(1, -100, -5)
print(item1.name)
print(item1.calculate_total_price())
# print(item1.calculate_total_price(item1.price, item1.quantity))



item1 = Item("Laptop", 1000, 3)
print(item1.name)
print(item1.calculate_total_price())
# item1.has_numpad  = False
# print(item1.has_numpad)