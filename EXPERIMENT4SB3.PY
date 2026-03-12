import matplotlib.pyplot as plt

# Departments and employee count
departments = ["HR", "IT", "Finance", "Marketing", "Operations"]
employees = [25, 60, 35, 40, 30]

# Create bar plot
plt.bar(departments, employees)

# Labels and title
plt.xlabel("Departments")
plt.ylabel("Number of Employees")
plt.title("Department-wise Employee Count")

# Display the plot
plt.show()