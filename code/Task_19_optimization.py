import numpy as np
from scipy.optimize import minimize

# Real-world case: Minimum-cost vehicle fleet
# Minimize Cost = 5000 * x1 + 8000 * x2
# Subject to: x1 + x2 >= 20 (total vehicles)
# x1 >= 5 (minimum small vehicles)
# x2 >= 3 (minimum large vehicles)

def cost_function(x):
    return 5000 * x[0] + 8000 * x[1]

# Constraints
constraints = (
    {'type': 'ineq', 'fun': lambda x: x[0] + x[1] - 20}, # x1 + x2 >= 20
    {'type': 'ineq', 'fun': lambda x: x[0] - 5},         # x1 >= 5
    {'type': 'ineq', 'fun': lambda x: x[1] - 3}          # x2 >= 3
)

# Bounds (non-negative)
bounds = ((0, None), (0, None))

# Initial guess
x0 = [10, 10]

# Solve
result = minimize(cost_function, x0, method='SLSQP', bounds=bounds, constraints=constraints)

print("Optimal fleet size (Small, Large):", np.round(result.x, 2))
print(f"Minimum cost: KES {result.fun:,.2f}")