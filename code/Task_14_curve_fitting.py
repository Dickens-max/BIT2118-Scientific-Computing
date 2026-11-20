import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# Real-world case: Product demand forecasting
# Price (x) vs Demand (y)
price = np.array([10, 15, 20, 25, 30])
demand = np.array([100, 80, 65, 50, 40])

# Define an exponential decay model: y = a * exp(b * x)
def demand_model(x, a, b):
    return a * np.exp(b * x)

# Fit the model to the data
popt, pcov = curve_fit(demand_model, price, demand)
a_fit, b_fit = popt

print(f"Fitted parameters: a = {a_fit:.2f}, b = {b_fit:.4f}")

# Predict demand at price = 22
predicted_demand = demand_model(22, *popt)
print(f"Predicted demand at price 22: {predicted_demand:.2f} units")