import cpmpy as cp

b = cp.boolvar(name="b")
x = cp.intvar(lb=1,ub=10, name="x")

B = cp.boolvar(shape=4, name="B")
print(B)  # [B[0] B[1] B[2] B[3]]

X = cp.intvar(1,10, shape=(2,2), name="X")
print(X)  # [[X[0,0] X[0,1]]
          #  [X[1,0] X[1,1]]]
