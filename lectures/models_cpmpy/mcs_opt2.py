import cpmpy as cp

def mcs_opt(constraints):
    maxcsp_model = cp.Model()

    maxcsp_model.maximize(cp.sum(constraints))  # maximize satisfied constraints
    maxcsp_model.solve()
    mcs = [c for c in constraints if c.value() is False]

    return mcs
