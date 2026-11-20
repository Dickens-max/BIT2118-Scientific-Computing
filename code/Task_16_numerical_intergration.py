import numpy as np
from scipy.integrate import trapezoid

# Real-world case: Distance travelled from speed readings
# Time (hours) and Speed (km/h)
time = np.array([0, 1, 2, 3, 4, 5], dtype=float)
speed = np.array([50, 60, 55, 70, 65, 80], dtype=float)

# Distance = integral of speed over time
distance = trapezoid(speed, time)

print(f"Total distance travelled: {distance:.2f} km")