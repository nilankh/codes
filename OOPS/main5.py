import csv


class Item:
    # class attributes are shared among all the instances of the class
    # class attributes are defined outside the __init__ method
    pay_rate = 0.8
    all = []
    def __init__(self, name: str, price: float,quantity=0):
        
        # Run validations to the received argumnets
        assert price >= 0, f"Price {price} is not valid"
        assert quantity >= 0, f"Quantity {quantity} is not valid"

        # these all are instance attributes, they are associated with the instance of the class
        self.__name = name
        self.__price = price
        self.quantity = quantity
        
        # Actions to execute
        Item.all.append(self)

    @property
    def price(self):
        return self.__price

    @property
    # property decorator = REad only attribute
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        self.__name = value

    def calculate_total_price(self):
        return self.__price * self.quantity
    
    def apply_discount(self):
        # self.price = self.price * Item.pay_rate
        # if we use Item.pay_rate, it will always use the class attribute, but if we use self.pay_rate, it will first look for the attribute on the instance itself, if it is not found, it will go ahead and look for the class attribute.
        self.__price = self.__price * self.pay_rate

    # class method is a method, that could be accssed from the class level only, it doesn't need the instance to be created. in this we need to pass cls as a first argument. that is a class reference
    @classmethod
    def instantite_from_csv(cls):
        with open("./OOPS/items.csv","r") as f:
            reader = csv.DictReader(f)
            items = list(reader)
        for item in items:
            Item(
                    name=item.get("name"),
                    price=float(item.get("price")), 
                    quantity=int(item.get("quantity"))
                )

    # in static method, we don't need to pass cls or self, it is just a normal function, but it is associated with the class
    @staticmethod
    def is_integer(num):
        # we will count out the floats that are point zero
        # for eg 5.0, 10.0
        if isinstance(num, float):
            # count out the floats that are point zero
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False
        

    # it means representing your objects
    def __repr__(self):
        return f"{self.__class__.__name__} {self.name} - INR {self.price} - {self.quantity} units"
    
    # @property
    # def read_only_name(self):
    #     return "NILANK"

