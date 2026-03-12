import matplotlib.pyplot as plt

# Product names
products = ["Product A", "Product B", "Product C", "Product D"]

# Sales values
sales = [150, 200, 120, 180]

# Create bar plot
plt.bar(products, sales)

# Labels and title
plt.xlabel("Products")
plt.ylabel("Sales")
plt.title("Sales of Four Products")

# Show plot
plt.show()