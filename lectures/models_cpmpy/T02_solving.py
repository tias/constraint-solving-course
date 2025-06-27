import cpmpy as cp

Xs = cp.intvar(1,10, shape=3)
m = cp.Model( cp.AllDifferent(Xs) )
m.maximize(cp.sum(Xs))

hassol = m.solve()
print("Status:", m.status())  # Status: ExitStatus.OPTIMAL (0.03033301 seconds)
if hassol:
    print(m.objective_value(), Xs.value())  # 27 [10  9  8]
else:
    print("No solution found.")
    print(m)  # pretty-prints the constraints in the model
