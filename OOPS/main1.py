class Item:
    # class attributes are shared among all the instances of the class
    # class attributes are defined outside the __init__ method
    pay_rate = 0.8 
    def __init__(self, name: str, price: float,quantity=0):
        
        assert price >= 0, f"Price {price} is not valid"
        assert quantity >= 0, f"Quantity {quantity} is not valid"

        # these all are instance attributes, they are associated with the instance of the class
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        # self.price = self.price * Item.pay_rate
        # if we use Item.pay_rate, it will always use the class attribute, but if we use self.pay_rate, it will first look for the attribute on the instance itself, if it is not found, it will go ahead and look for the class attribute.
        self.price = self.price * self.pay_rate

        
# item1 = Item(1, 100, 5)
# item2 = Item("Laptop", 1000, 3)

# print(Item.pay_rate)
# print(item1.pay_rate)
# print(item2.pay_rate)
# # so for each instance, first it willl try to find the pay_rate on the instance itself, if it is not found, it will go ahead and look for the class attribute.


# print(Item.__dict__) # it will show all the class attributes
# print(item1.__dict__) # it will show all the instance attributes


item1 = Item("Phone", 100, 5)
item1.apply_discount()
print(item1.price)

# suppose for second item, i want to change the pay_rate
item2 = Item("Laptop", 1000, 3)
item2.pay_rate = 0.7
item2.apply_discount()
print(item2.price)