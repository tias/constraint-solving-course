import cpmpy as cp

n = 101


X = cp.intvar(0, n - 1, shape=(n,))

model = cp.Model(
    cp.GlobalCardinalityCount(X, list(range(n)), X),
)

model.solve()
print(X.value())
print(model.status())

model += cp.sum(X) == n
model += cp.sum(i * x for i, x in enumerate(X)) == n
# model += cp.sum(X[i] * X[X[i]] for i in range(n)) == n

model.solve()
print(X.value())
print(model.status())
