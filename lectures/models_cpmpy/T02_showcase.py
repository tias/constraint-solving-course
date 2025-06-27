import cpmpy as cp
m = cp.Model()

# Decision variables
b = cp.boolvar(name="b")
X = cp.intvar(1,10, shape=3, name="X")

# Constraints
m.add(X[0] == 1)
m.add(cp.AllDifferent(X))
m.add(b.implies(X[1] + X[2] > 5))

# Objective function (optional)
m.maximize(cp.sum(X) + 100*b)

if m.solve():
    print(X.value(), b.value())
    print("obj:", m.objective_value())
else:
    print("No solution found.")
    print(m)
