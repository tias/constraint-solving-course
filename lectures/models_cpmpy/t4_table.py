import cpmpy as cp

# Define variables (W1 and W2 can take values: 1, 2, or 3 for shifts)
W1 = cp.intvar(1, 3, name="W1")
W2 = cp.intvar(1, 3, name="W2")

# Define the model with the Table constraint
model = cp.Model()

# Allowed combinations of shifts (table of allowed tuples)
T = [(1, 2), (1, 3), (2, 3)]
model.add(cp.Table([W1, W2], T))

# Solve the model
if model.solve():
    print(f"W1: {W1.value()}, W2: {W2.value()}")
else:
    print("No solution found")
