import numpy as np
from scipy.optimize import fsolve

# Real-world case: Overlapping cell-tower coverage
# Two towers with coverage equations:
# Tower 1: (x - 0)^2 + (y - 0)^2 = 5^2 (radius 5)
# Tower 2: (x - 6)^2 + (y - 0)^2 = 4^2 (radius 4)
# We find where the boundaries intersect

def equations(vars):
    x, y = vars
    eq1 = x**2 + y**2 - 25
    eq2 = (x - 6)**2 + y**2 - 16
    return [eq1, eq2]

# Initial guess
initial_guess = [3, 2]
solution = fsolve(equations, initial_guess)

print("Intersection point (x, y):", np.round(solution, 4))
print("Distance check to Tower 1:", np.round(np.sqrt(solution[0]**2 + solution[1]**2), 4))
print("Distance check to Tower 2:", np.round(np.sqrt((solution[0]-6)**2 + solution[1]**2), 4))