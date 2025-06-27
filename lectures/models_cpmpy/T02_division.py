import cpmpy as cp
m = cp.Model()
X = cp.intvar(1,9, shape=10)
b = 9
m.add(cp.sum(X) >= 25)

m.minimize(cp.sum(X) // len(X));  # minimise the average (integer division)
m.solve()
print(m.objective_value())

m.minimize(cp.sum(X));  # minimise without the constant division
m.solve()
print(m.objective_value() / len(X))  # print with normalisation (float division)


m.add(cp.sum(X) >= (2/3)*b)

m.add(3*cp.sum(X) >= 2*b)
