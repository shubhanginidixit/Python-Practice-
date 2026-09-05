import matplotlib.pyplot as plt
import pandas as pd

# Data for Bar Plot
subjects = ["Math", "Science", "English", "Computer", "History"]
marks = [85, 78, 90, 88, 76]

# Create Bar Plot
plt.bar(subjects, marks)
plt.title("Marks in Different Subjects")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.show()

# Data for Scatter Plot
study_hours = [1, 2, 3, 4, 5, 6]
marks_obtained = [40, 50, 60, 65, 80, 90]

# Create Scatter Plot
plt.scatter(study_hours, marks_obtained)
plt.title("Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks Obtained")
plt.show()