import cpmpy as cp

Edges = [(0,1), (0,4), (1,3), (2,3)]

num_nodes = 5

# Create a variable for each node representing its colour
nodes = cp.intvar(0, num_nodes-1, shape=num_nodes, name="nodes")

model = cp.Model()

# Adjacent vertices must have different colours
model.add([nodes[i] != nodes[j] for (i, j) in Edges])
# Minimize nr of unique colours used
model.minimize(cp.NValue(nodes))

# Solve the model
if model.solve():
    print("Solution found:")
    for i in range(num_nodes):
        print(f"Node {i} has colour {nodes[i].value()}")
else:
    print("No solution found with the given number of colours.")
