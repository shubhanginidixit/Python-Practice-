import matplotlib.pyplot as plt

# Data
years = [2019, 2020, 2021, 2022, 2023]
population = [500000, 520000, 545000, 570000, 600000]

# Create bar chart
plt.bar(years, population)

# Labels and title
plt.xlabel("Years")
plt.ylabel("Population")
plt.title("City Population Growth Over Five Years")

# Display chart
plt.show()