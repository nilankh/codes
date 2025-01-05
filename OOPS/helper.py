# when to use class methods and when to use static methods?


# we will use static method, when we want to do something that should not be unique per instance
class Item:
    @staticmethod
    def is_integer():

        '''
            This should do something that has a realtionship with the class, but not something that must be unique per instance
        '''

    @classmethod
    def instantiate_from_something(cls):
        '''
            This should also do something that has a relationship with the class, but usually, those are used to manipulate different structures of data to instantiate objects, like we have done with csv
        '''

'''
    Only main difference between class method and static method is the static methods are not passing the object reference as the first argument in the background, Static methods can be called on the class itself or on an instance. But class methods A class method can access and modify class attributes (shared among all instances) but cannot directly access instance attributes. Class methods operates on the class itself, not the specific instance.
'''