class Student:
    def __init__(self, name=str, score=int, matric_no=str):
        self.name = name  # Public Variable: accessed within and outside the class
        self._score = score  # Protected Variable: accessed only within the class and its subclasses
        self.__matric_no = matric_no  # Private Variable: accessed only within the class

    @property  # This is a Getter: it reads the value already assigned to the attribute
    def score(self):
        return self._score

    # Protected Method: can only be called by other methods in the same class and its subclasses
    @score.setter  # This is a setter: it puts a new value for the attribute
    def score(self, value):
        if not isinstance(value, int):
            raise TypeError("Score must be an integer")
        self._score = value

    # Method Overloading is when you a function with the same name but collects different parameters/arguments. and to use the @overload decorator you have to import overload using: from typing import overload

    # Private Method: can only be called by other methods in same class; can't be accessed by its subclass
    def __display(self):
        print('Name: {}, Score: {}, Matric No.: {}'.format(
            self.name, self._score, self.__matric_no))

    # Public Metod: here's a Public Method calling the Private Method
    def display(self):
        self.__display()


if __name__ == '__main__':
    s = Student('John', 87, '070922001')
    print(s.display())  # calling the Public method to print from Private method
    print(s.score)  # using the Getter to print the score.
    s.score = 77  # calling the Setter by passing an integer to modify the score
    print(s.score)  # printing the modified score
    print('\nScore has been changed to {}\n'.format(s.score))
    s.display()
    print(s.__matric_no)  # doesn't work because __matric.no is a private variable
    print(s.__display())  # doesn't work because __display() is a private method
