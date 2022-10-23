# For Multiple Inheritance, a Child class inherits from Multiple Parent classes

# Parent Class
class Vehicle:  # defining the Parent class
    def __init__(self, name, color, price):
        self.name = name
        self.color = color
        self.price = price

    def display(self):  # defining a parent class method
        print('Name:', self.name)

    def vehicle_info(self):  # defining a parent class method
        print(f"Color: {self.color}; Price: {self.price}")

# Child Class


class Car(Vehicle):  # inheriting from the Parent class Vehicle
    def __init__(self, name, color, price, model):
        # indicating you are initailizing and inheriting all from the constructor
        super().__init__(name, color, price)
        self.model = model  # then define the additional parameter

    # Polymorphism (or Method Overriding):
    '''
    Note: the child class overrides the parent method: display() method being overridden by printing both name (from Parent) and model (from Child class).
    '''
    def display(self):  # defining a child class method
        print(f"Name: {self.name}; Model: {self.model}")

    def car_info(self):  # defining a child class method
        print(f"Model: {self.model}\nPrice: {self.price}")


# if __name__ == "__main__":
#     car = Car("BMW", "White", "50000", "X5")
#     car.display()
#     car.car_info()
#     car.vehicle_info()

car = Car("BMW", "White", "50000", "X5")
car.display()
car.car_info()
car.vehicle_info()
