# Instance variable / Static variable


class Student:

    def __init__(self, name, age):
        self.name = name  # Instance variable is made inside constructor of the class
        self.age = age    # Instance variable

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Instance var creates seperate memory for each objects
obj1 = Student("Hardeep", 20)
obj2 = Student("Siddhu", 22)

obj1.display_info()
obj2.display_info()

obj1.age = 21
print("After updating obj1's age:")

obj1.display_info()
obj2.display_info()
