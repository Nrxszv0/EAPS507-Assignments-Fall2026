import matplotlib.pyplot as plt
import numpy as np

# Illustrative daily temperatures (degrees Celsius)
temperature = np.array([20, 22, 24, 21, 25, 27, 23])

mean_temp = np.mean(temperature)
print(f"Mean temperature: {mean_temp:.2f} °C")

plt.plot(range(1, 8), temperature, marker="o")
plt.xlabel("Day")
plt.ylabel("Temperature (°C)")
plt.title("Daily Temperature Variation")
plt.grid(True)
plt.show()