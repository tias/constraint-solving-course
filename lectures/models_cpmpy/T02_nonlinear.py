import cpmpy as cp
m = cp.Model()
n = 5
b = 3

X = cp.intvar(0,1, shape=n)
Y = cp.intvar(0,1, shape=n)
m.add(cp.Count(X*Y, 1) == b)

X = cp.intvar(0,1, shape=n)
Y = cp.intvar(0,1, shape=n)
m.add(cp.Count(X+Y, 2) == b)
