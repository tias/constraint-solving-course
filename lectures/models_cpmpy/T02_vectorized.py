import cpmpy as cp

X = cp.intvar(1,9, shape=3, name="X")
A = [1,2,4]

print(X == A)  # output: [X[0]==1 X[1]==2 X[2]==4]

print(X == 3)  # output: [X[0]==3 X[1]==3 X[2]==3]
