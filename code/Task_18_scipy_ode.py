import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Real-world case: SIR epidemic model
# S: Susceptible, I: Infected, R: Recovered
# dS/dt = -beta * S * I / N
# dI/dt = beta * S * I / N - gamma * I
# dR/dt = gamma * I

N = 1000
beta = 0.3
gamma = 0.1

def sir_model(t, y):
    S, I, R = y
    dS = -beta * S * I / N
    dI = beta * S * I / N - gamma * I
    dR = gamma * I
    return [dS, dI, dR]

# Initial conditions: 1 infected, 999 susceptible
y0 = [999, 1, 0]
t_span = (0, 100)
t_eval = np.linspace(0, 100, 200)

sol = solve_ivp(sir_model, t_span, y0, t_eval=t_eval)

print("Peak infected at day:", sol.t[np.argmax(sol.y[1])])
print("Peak infected count:", int(np.max(sol.y[1])))