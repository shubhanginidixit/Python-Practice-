pyimport matplotlib.pyplot as plt

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday","Saturday","Sunday"]
temperature = [30, 32, 31, 29, 33,22,35]

plt.plot(days, temperature, marker='o', linestyle='-', color='pink', label='Temperature')

plt.title("Temperature Trend over Week")
plt.xlabel("Days")
plt.ylabel("Temperature")

plt.legend()
plt.grid(True)

plt.show()