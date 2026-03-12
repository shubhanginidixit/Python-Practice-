import matplotlib.pyplot as plt

# Data
advertising_spend = [1000, 2000, 3000, 4000, 5000]
sales_revenue = [15000, 18000, 22000, 26000, 30000]

# Create scatter plot
plt.scatter(advertising_spend, sales_revenue)

# Labels and title
plt.xlabel("Advertising Spend")
plt.ylabel("Sales Revenue")
plt.title("Advertising Spend vs Sales Revenue")

# Display plot
plt.show()