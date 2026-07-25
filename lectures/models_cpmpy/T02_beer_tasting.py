import cpmpy as cp
m = cp.Model()

# Create six (named) Boolean variables, where `X[i]` is True iff we try beer `i`
X = cp.boolvar(shape=6, name=["Stella", "Duvel", "Vedett", "Karmeliet", "Carolus", "Kriek"])
st, du, vi, tk, gc, kl = X  # "Unpack" the variables

# Constraint: Try less than 4 Stella's worth
m.add(52*st + 85*du + 60*vi + 84*tk + 117*gc + 35*kl <= 4*52)
# Objective: Maximize the must-try factor
m.maximize(50*st + 80*du + 75*vi + 82*tk + 95*gc + 70*kl)      

m.solve()
print(m.status())
print(", ".join(str(x) for x in X if x.value() is True), f"({m.objective_value()})")

# m.solveAll(display=lambda : print(", ".join(f"{x}={x.value()}" for x in X)))
