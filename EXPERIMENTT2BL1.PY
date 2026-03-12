# Custom Class Creation

class Student:
    # Class variable
    school_name = "ABC School"

    # Constructor with instance variables
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Member method
    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("School:", Student.school_name)


# Object creation
s1 = Student("Rahul", 18)
s2 = Student("Priya", 17)

# Accessing variables and calling methods
s1.display()
print()
s2.display()