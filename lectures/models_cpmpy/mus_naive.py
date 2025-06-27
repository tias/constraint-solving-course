import cpmpy as cp


def mus_naive(constraints):
    m = cp.Model(constraints)
    assert m.solve() is False, "Model should be UNSAT"

    core = constraints
    i = 0
    while i < len(core):
        subcore = core[:i] + core[i + 1:]  # try all but constraint 'i'
        if cp.Model(subcore).solve() is True:
            i += 1  # removing 'i' makes it SAT, need to keep for UNSAT
        else:
            core = subcore  # can safely delete 'i'
    return core
