import matplotlib.pyplot as plt
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
temperature = [30, 32, 31, 29, 33]
plt.plot(days, temperature, marker='o', linestyle='-', color='blue', label='Temperature')
plt.title("Temperature Trend Over a Week")
plt.xlabel("Days")
plt.ylabel("Temperature (°C)")
plt.legend()
plt.grid(True)
plt.show()