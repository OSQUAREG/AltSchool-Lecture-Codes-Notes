# Example 3: INHERITANCE

# parent class
class Bird:
    def __init__(self, name):
        self.__name = name
        print("Bird is ready")

    def whoisThis(self):
        print("Bird")

    def swim(self):
        print("Swim faster")
    
    def beauty(self):
        print("{} is a beautiful bird".format(self.__name))
    
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

peggy = Penguin("Peggy")
peggy.whoisThis()
peggy.swim()
peggy.run()
peggy.beauty()