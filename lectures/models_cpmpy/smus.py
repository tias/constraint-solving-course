from cpmpy.tools.explain.mus import optimal_mus

def smus(soft, hard=[], solver="ortools", hs_solver="ortools"):
    return optimal_mus(soft, hard=hard, weights=None, solver=solver,
    hs_solver=hs_solver)