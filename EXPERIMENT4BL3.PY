import matplotlib.pyplot as plt

# Dataset
subjects = ["Math", "Science", "English", "History"]
average_marks = [85, 90, 78, 88]

# Create bar plot
plt.bar(subjects, average_marks)

# Labels and title
plt.xlabel("Subjects")
plt.ylabel("Average Marks")
plt.title("Average Marks of Subjects")

# Display the graph
plt.show()