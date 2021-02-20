class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(self.name, self.age)    

peter = Person('Peter', 35)        
peter.show()
