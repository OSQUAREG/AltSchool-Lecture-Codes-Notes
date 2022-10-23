from datetime import date

class Student: # defining the class using the keyword "class"
    # Class Variables: defined outside the constructor but within the class
    school_name: str = "AltSchool Africa"

    # Constructor to Initialize the Object
    def __init__(self, name: str, course: str, age: int):
        self.name = name
        self.course = course
        self.age = age

    # Instance Method: uses parameters from the constructor
    def show(self):
        return f"Student Name: {self.name}; Course: {self.course}; Age: {self.age}"

    # Static Method: does not interact/modify any object from the class. Uses the decorator @staticmethod
    @staticmethod
    def is_adult(age: int) -> bool:
        return age >= 18

    # Class Method: to use a class variable, wrap the function in a docorator @classmethod, with cls as the parameter.
    @classmethod # can interact with the class variable
    def get_school_name(cls):
        return cls.school_name

    @classmethod # can also interact with the other objects in the class
    def get_age_from_birth_year(cls, name: str, course: str, birth_year: int):
        return f'Name: {name}, Course: {course}, Age: {date.today().year - birth_year}'


# Testing the Class objects
student = Student('Greg', 'Python', 27)
print(student.name)
print(student.course)
print(student.age)
print(student.show())

# Testing the static method
print(student.is_adult(35))

if Student.is_adult(20):
    print('This student is an adult')
else:
    print('This student is not an adult')

# Testing the class method
print(Student.get_school_name())
print(Student.get_age_from_birth_year('Austin', 'Python', 1995))
