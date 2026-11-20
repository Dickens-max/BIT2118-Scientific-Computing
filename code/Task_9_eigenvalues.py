import numpy as np

# Define a sample adjacency matrix for an office network (5 nodes)
# 1 means a direct connection, 0 means no connection
adj_matrix = np.array([
    [0, 1, 1, 0, 0],
    [1, 0, 1, 0, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 1, 0, 1],
    [0, 0, 0, 1, 0]
], dtype=float)

# Calculate eigenvalues and right eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(adj_matrix)

print("Eigenvalues:\n", eigenvalues)
print("\nPrincipal Eigenvector (Node Importance):\n", np.round(np.abs(eigenvectors[:, 0]), 4))

# Note: The eigenvector associated with the largest eigenvalue 
# indicates the most important node in the network.