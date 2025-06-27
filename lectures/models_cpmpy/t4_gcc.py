import cpmpy as cp

# Number of customer locations
n_locations = 10
n_warehouses = 5
# Variables: for each customer location, we assign a warehouse (1 to 5)
assignments = cp.intvar(0, n_warehouses-1, shape=n_locations, name="assignments")
model = cp.Model()

# Define the capacities of the warehouses
capacities = [3, 2, 2, 1, 2]  # Max customers each warehouse can serve

# GlobalCardinalityCount constraint to ensure each warehouse is assigned correctly
model.add(cp.GlobalCardinalityCount(assignments, list(range(n_warehouses)), capacities))

# Solve the model
model.solve()
