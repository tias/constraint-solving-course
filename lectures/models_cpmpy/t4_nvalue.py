from cpmpy import *

Edges = [(0,1), (0,4), (1,3), (2,3)]

num_nodes = 5

# Create a variable for each node representing its color
nodes = intvar(0, num_nodes-1, shape=num_nodes, name="nodes")

model = Model()

# Adjacent vertices must have different colors
model.add([nodes[i] != nodes[j] for (i, j) in Edges])
# Minimize distinct colours used
model.minimize(NValue(nodes))

# Solve the model
if model.solve():
    print("Solution found:")
    for i in range(num_nodes):
        print(f"Node {i} has color {nodes[i].value()}")
else:
    print("No solution found with the given number of colors.")