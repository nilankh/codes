class Item:
    # need of self, python passes the object itself as a first argument, when you go ahead and call those methods. Now, if i item1.calculate_total_price() is called, python will pass item1 as a first argument to calculate_total_price method.
    def  calculate_total_price(self, price, quantity):
        return price * quantity

item1 = Item()
item1.name = "phone"
item1.price = 100
item1.quantity = 5
print(item1.calculate_total_price(item1.price, item1.quantity))
# print(type(item1))
# print(type(item1.name))
# print(type(item1.price))
# print(type(item1.quantity))

item1 = Item()
item1.name = "Laptop"
item1.price = 1000
item1.quantity = 3
print(item1.calculate_total_price(item1.price, item1.quantity))