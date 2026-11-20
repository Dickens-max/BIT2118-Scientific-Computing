import numpy as np
import matplotlib.pyplot as plt

# Setup the problem
n = 5
A = np.diag([2.0]*n) + np.diag([-1.0]*(n-1), 1) + np.diag([-1.0]*(n-1), -1)
b = np.array([100., 0., 0., 0., 20.])
tol = 1e-8
max_iter = 500

# Jacobi Method
x_jacobi = np.zeros(n)
jacobi_errors = []
for k in range(max_iter):
    x_new = np.zeros(n)
    for i in range(n):
        s = sum(A[i, j] * x_jacobi[j] for j in range(n) if j != i)
        x_new[i] = (b[i] - s) / A[i, i]
    err = np.max(np.abs(x_new - x_jacobi))
    jacobi_errors.append(err)
    x_jacobi = x_new
    if err < tol:
        jacobi_iters = k + 1
        break

# Gauss-Seidel Method
x_gs = np.zeros(n)
gs_errors = []
for k in range(max_iter):
    x_old = x_gs.copy()
    for i in range(n):
        s = sum(A[i, j] * x_gs[j] for j in range(n) if j != i)
        x_gs[i] = (b[i] - s) / A[i, i]
    err = np.max(np.abs(x_gs - x_old))
    gs_errors.append(err)
    if err < tol:
        gs_iters = k + 1
        break

# Direct Solution
x_direct = np.linalg.solve(A, b)

# Print outputs
print("Jacobi temperatures:", np.round(x_jacobi, 4))
print("Gauss-Seidel temperatures:", np.round(x_gs, 4))
print("Direct solution:", np.round(x_direct, 4))
print(f"Jacobi iterations: {jacobi_iters} | Gauss-Seidel iterations: {gs_iters}")

# Plotting the convergence
plt.figure(figsize=(8, 6))
plt.plot(jacobi_errors, label='Jacobi')
plt.plot(gs_errors, label='Gauss-Seidel')
plt.yscale('log')
plt.xlabel('Iteration')
plt.ylabel('Error')
plt.title('Convergence of iterative temperature solution')
plt.legend()
plt.grid(True)
plt.show()