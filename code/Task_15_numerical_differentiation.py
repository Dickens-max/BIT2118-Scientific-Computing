import numpy as np

# Real-world case: Acceleration from velocity data
# Time (s) and Velocity (m/s)
time = np.array([0, 1, 2, 3, 4, 5], dtype=float)
velocity = np.array([0, 3, 7, 12, 18, 25], dtype=float)

# Calculate acceleration using central differences (np.gradient)
# a = dv/dt
acceleration = np.gradient(velocity, time)

print("Time (s):", time)
print("Velocity (m/s):", velocity)
print("Acceleration (m/s^2):", acceleration)