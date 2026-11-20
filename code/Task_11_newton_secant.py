import numpy as np

# Real-world case: True interest rate of a loan
# Using Newton-Raphson to find IRR
# Cash flows: [-1000 (loan), 300, 300, 300, 300] (repayments)
cash_flows = np.array([-1000, 300, 300, 300, 300])

def npv(r):
    return sum(cf / (1 + r)**t for t, cf in enumerate(cash_flows))

def npv_derivative(r):
    return sum(-t * cf / (1 + r)**(t + 1) for t, cf in enumerate(cash_flows))

def newton_raphson(r_init, tol=1e-6, max_iter=100):
    r = r_init
    for i in range(max_iter):
        f = npv(r)
        df = npv_derivative(r)
        if df == 0:
            print("Zero derivative. No solution found.")
            return None
        r_new = r - f / df
        if abs(r_new - r) < tol:
            return r_new
        r = r_new
    print("Did not converge")
    return None

true_rate = newton_raphson(0.1)
print(f"True interest rate (IRR): {true_rate:.4%}")