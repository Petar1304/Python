# Object Oriented Programming in Python
import csv

class Item:
    # class attributes
    pay_rate = 0.8 # access it with Item.pay_rate
    all = []

    # magic mathods
    def __init__(self, name: str, price: float, quantity: int):
        
        # Run validation to the recieved arguments
        assert price >= 0, f"Price {price} is not greater then zero"
        assert quantity >= 0, f"Quantity {quantity} is no greater then zero"

        # Assign to self object
        self.__name = name # make smt private by adding __ in front
        self.price = price
        self.quantity = quantity
        # Actions to excecute
        Item.all.append(self)

    @property
    def getName(self):
        return self.__name

    @__name.setter
    def __name(self, value):
        self.__name = value

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def getPrice(self):
        return self.price * self.quantity * Item.pay_rate

    # with out self, method for whole class(static)
    @classmethod
    def instantiate_from_csv(cls): # recieve class as parameter
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity')),
            )

    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

# Inheritance
class Phone(Item):
    def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
        # Call to super function to have access to all attributes / methods
        super().__init__(name, price, quantity)
        # Run validations to the received arguments
        assert broken_phones >= 0, f"Broken Phones {broken_phones} is not greater or equal to zero!"
        # Assign to self object
        self.broken_phones = broken_phones

Item.instantiate_from_csv()
print(Item.all)
print(Item.is_integer(7.1))
phone1 = Phone("jscPhonev10", 500, 5, 1)
