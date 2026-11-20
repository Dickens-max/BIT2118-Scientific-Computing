import numpy as np
import matplotlib.pyplot as plt

# Real-world case: Logistic population growth
# dP/dt = r * P * (1 - P/K)
r = 0.1   # Growth rate
K = 1000  # Carrying capacity
P0 = 10   # Initial population
dt = 0.1  # Time step
t_max = 100

t = np.arange(0, t_max, dt)
P = np.zeros(len(t))
P[0] = P0

for i in range(1, len(t)):
    dP = r * P[i-1] * (1 - P[i-1]/K)
    P[i] = P[i-1] + dP * dt

print(f"Population after {t_max} days: {P[-1]:.2f}")
# plt.plot(t, P) # Uncomment to plot