# For Multiple Inheritance, a Child class inherits from Multiple Parent classes

# Parent Class 1
class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def get_person_info(self): # defining a parent method
        print(f"the name is {self.name} and the age is {self.age}")

    @staticmethod
    def random_method():
        return f"This is a random method from Person"

# Parent Class 2
class School:
    def __init__(self, school_name: str, school_location: str):
        self.school_name = school_name
        self.school_location = school_location

    def get_school_info(self): # defining a parent method
        print(f"{self.school_name} is in {self.school_location}")

    @staticmethod
    def random_method():
        return f"This is a random method from School"

# Child Class
class Student(Person, School): # inheriting from the Parent classes: Person and School class
    def __init__(self, name: str, age: int, school_name: str, school_location: int):
        Person.__init__(self, name, age)
        School.__init__(self, school_name, school_location)

    def get_student_info(self):
        print(f"{self.name} attends {self.school_name} in {self.school_location}")


# if __name__ == "__main__":
#     student = Student("Austin", 27, "AltSchool Africa", "California")
#     student.get_person_info()
#     student.get_school_info()
#     student.get_student_info()
#     print(student.random_method())

student = Student("Austin", 27, "AltSchool Africa", "California")
student.get_person_info()
student.get_school_info()
student.get_student_info()
print(student.random_method())

''' 
NOTE:
In Python, when both Parent classes share the same method definition, the Child class inherits from the left to right, prioritising the leftmost Parent class called when defining the subclass. In this case, it's the Person class before School class in the child class Student(Person, School).
'''
