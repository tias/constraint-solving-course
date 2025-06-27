import cpmpy as cp

def mcs_opt(constraints):

    maxcsp_model = cp.Model()
    B = cp.boolvar(shape=len(constraints))  # Boolean indicator variable for each constraint
    maxcsp_model.add(B.implies(constraints))  # reify constraints (vectorized)

    maxcsp_model.maximize(cp.sum(B))  # maximize satisfied constraints
    maxcsp_model.solve()

    mcs = [c for b,c in zip(B, constraints) if b.value() is False]
    return mcs
