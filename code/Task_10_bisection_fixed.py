import numpy as np

# Real-world case: Business break-even point
# Cost function: C(x) = 500 + 10x (Fixed cost 500, variable cost 10)
# Revenue function: R(x) = 25x (Selling price 25)
# Profit function: P(x) = R(x) - C(x) = 15x - 500
# We want to find x where P(x) = 0

def profit(x):
    return 15 * x - 500

def bisection_method(func, a, b, tol=1e-5):
    if func(a) * func(b) >= 0:
        print("Bisection method fails. No root in the interval.")
        return None
    
    c = a
    while (b - a) >= tol:
        c = (a + b) / 2.0
        
        if func(c) == 0.0:
            break
        if func(c) * func(a) < 0:
            b = c
        else:
            a = c
    return c

# Initial interval [0, 100]
breakeven_units = bisection_method(profit, 0, 100)
print(f"Break-even point: {breakeven_units:.2f} units")