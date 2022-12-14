# DRY (Don't Repeat Yourself).

# # Example 1: using CLASS and INSTANCE Attributes
# class Parrot:
#     # class attribute/variable
#     species = "bird"

#     # instance attribute
#     def __init__(self, name, age, color):
#         self.name = name
#         self.age = age
#         self.color = color

# blu = Parrot('Blu', 10, 'Blue')
# woo = Parrot('Woo', 15, 'Red')

# print("Blu is a {}".format(blu.__class__.species))
# print("Woo is a {}".format(woo.__class__.species))

# print("{} is {} years old, and has a color of {}".format(blu.name, blu.age, blu.color))
# print("{} is {} years old, and has a color of {}".format(woo.name, woo.age, woo.color))

# # Example 2: using INSTANCE Methods
# class Parrot:
#     # instance attributes
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     # instance method1
#     def sing(self, song):
#         return "{} sings {} and {} years old".format(self.name, song, self.age)

#     # instance method2
#     def dance(self):
#         return "{} is now dancing".format(self.name)

# # instantiate the object
# blu = Parrot("Blu", 10)

# # call our instance methods
# print(blu.sing("'Happy'"))
# print(blu.dance())


# # Example 3: showing INHERITANCE

# parent class
# class Bird:
#     def __init__(self):
#         print("Bird is ready")

#     def whoisThis(self):
#         print("Bird")

#     def swim(self):
#         print("Swim faster")

# child class
class Penguin(Bird):

    def __init__(self):
        # call super() function - tells python that you are initailizing from the parent with __init__
        super().__init__()
        print("Penguin is ready")

    def whoisThis(self):
        print("Penguin")

    def run(self):
        print("Run faster")

    def beauty(self, name):
        self.name = name
        print("{} is a beautiful bird".format(self.name))


# peggy = Penguin()
# peggy.whoisThis()
# peggy.swim()
# peggy.run()
# peggy.beauty("Peggy")


# # Example 3: showing ENCAPSULATION
# # this restrict access to directly change variables in a class
# class Computer:
#     def __init__(self):
#         self.__maxprice = 900

#     def sell(self):
#         print("Selling Price: {}".format(self.__maxprice))

#     def setMaxPrice(self, price):
#         self.__maxprice = price

# c = Computer()
# c.sell()

# # trying to change the price
# c.__maxprice = 1000
# c.sell()

# # using the function setmaxprice
# c.setMaxPrice(1000)
# c.sell()

# c.setMaxPrice(2000)
# c.sell()


# # Example 4: showing POLYMORPHISM
# # ability to use common interface/attribute multiple times

# class Parrot:
#     def fly(self):
#         print("Parrot can fly")

#     def swim(self):
#         print("Parrot can't swim")

# class Penguin:
#     def fly(self):
#         print("Penguin can't fly")

#     def swim(self):
#         print("Penguin can swim")

# # common interface
# def flying_test(bird):
#     bird.fly()
#     print("Flying test complete")

# def swimming_test(bird):
#     bird.swim()
#     print("Swimming test complete")

# # instantiate objects
# blu = Parrot()
# peggy = Penguin()

# # passing the object
# flying_test(blu)
# flying_test(peggy)

# swimming_test(blu)
# swimming_test(peggy)


# # Example 5: showing the INSTANCE, CLASS and STATIC methodS
# class Student:
#     # class variable
#     school_name = "King's College"

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     # Instance Method
#     def show(self):
#         print('Student:', self.name, self.age)
#         print('School:', self.school_name)

#     # Class Method
#     @classmethod
#     def change_school(cls, name): # the first argument is recognised as self, even if you use a different name.
#         print('Previous School Name:', cls.school_name)
#         cls.school_name = name
#         print('School Name changed to:', Student.school_name)

#     # Static Method
#     @staticmethod # they are used for function that does not need a class to change
#     def find_note(subject_name):
#         print(subject_name, ':', ['chapter 1', 'chapter 2', 'chapter 3'])

# stud1 = Student('Greg', 20)
# stud1.show()
# stud1.change_school("Queen's College")
# stud1.find_note('Biology')
