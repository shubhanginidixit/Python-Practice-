# Student class

class Student:
    # Constructor
    def __init__(self, name, roll_no, course, marks):
        self.name = name
        self.roll_no = roll_no
        self.course = course
        self.marks = marks

    # Method to display details
    def display_details(self):
        print("Student Details")
        print("Name:", self.name)
        print("Roll No:", self.roll_no)
        print("Course:", self.course)
        print("Marks:", self.marks)


# Creating object
s1 = Student("Dhruv", 101, "Computer Science", 88)

# Display student details
s1.display_details()