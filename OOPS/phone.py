from main5 import Item

class Phone(Item):
     def __init__(self, name: str, price: float,quantity=0 ,broken_phones = 0):
        # all = []
        # Call to super function to have access to all attributes / methods
        super().__init__(name, price, quantity)

        # no need to use neeche wala code redundant ho jayega just use supper fuction


        # Run validations to the received argumnets
        # assert price >= 0, f"Price {price} is not valid"
        # assert quantity >= 0, f"Quantity {quantity} is not valid"
        assert broken_phones >= 0, f"Broken Phones {broken_phones} is not valid"

        # these all are instance attributes, they are associated with the instance of the class
        # self.name = name
        # self.price = price
        # self.quantity = quantity
        self.broken_phones = broken_phones
        
        # Actions to execute
        # Phone.all.append(self)
