'''
Abstraction is like telling you how to use a machine but not telling you how it works.
'''

from abc import ABC, abstractmethod
from math import pi
from xml.etree.ElementTree import PI

# Abstract Parent Class


class Shape(ABC):  # an Abstract Parent class inheriting from ABC (the Abstract base class in Python)

    @abstractmethod  # Decorator for Abstract Method
    def area(self):  # defining an Abstract Method
        pass

    @abstractmethod
    def volume(self):  # defining an Abstract Method
        pass


'''
NOTE: When inheriting from an Abstract Class, you must implement all of its methods. If any is omitted your code will throw an error.
'''

# Abstract Child Class


class Square(Shape):  # inherits from abstract class Shape.
    def __init__(self, side):  # becaus eall the sides of a square are equal
        self.side = side

    def area(self):
        return self.side * self.side  # same as: return self.side ** 2

    def volume(self):
        return self.side * self.side * self.side  # same as: return self.side ** 3


class Circle(Shape):  # inherits from abstract class Shape.
    PI = 3.14  # Class Constant

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        # same as: return (self.radius ** 2) * self.PI
        return self.radius * self.radius * self.PI

    def volume(self):
        # same as: return (self.radius ** 3) * self.PI
        return self.radius * self.radius * self.radius * self.PI


# if __name__ == "__main__":
#     square = Square(4)
#     print(f'The Area of this square is {square.area()}. \nThe Volume of this square is {square.volume()}\n')

#     circle = Circle(4)
#     print(f"The Area of this circle is {circle.area()}. \nThe Volume of this circle is {circle.volume()}\n")

square = Square(4)
print(
    f'The Area of this square is {square.area()}. \nThe Volume of this square is {square.volume()}\n')

circle = Circle(4)
print(
    f"The Area of this circle is {circle.area()}. \nThe Volume of this circle is {circle.volume()}\n")
