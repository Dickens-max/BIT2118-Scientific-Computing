import numpy as np

# Real-world case: Server-cluster reliability
# A cluster has 10 servers. Each server has a 95% chance of being online.
# The cluster works if at least 8 servers are online.
# Use Monte Carlo to estimate the probability.

num_simulations = 100_000
num_servers = 10
prob_online = 0.95
min_servers_required = 8

# Simulate: 1 for online, 0 for offline
simulations = np.random.choice([1, 0], size=(num_simulations, num_servers), p=[prob_online, 1-prob_online])

# Count servers online in each simulation
servers_online = np.sum(simulations, axis=1)

# Check success condition
successes = np.sum(servers_online >= min_servers_required)

reliability = successes / num_simulations

print(f"Estimated cluster reliability: {reliability:.4%}")