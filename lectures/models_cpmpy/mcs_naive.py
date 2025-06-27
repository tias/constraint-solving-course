import cpmpy as cp

def mcs_naive(constraints):
    mss = []  # grow a satisfiable subset one-by-one
    mcs = []  # everything else is in the minimum conflict set

    for cons in constraints:
        if cp.Model(mss + [cons]).solve():
            mss.append(cons)  # adding it remains SAT
        else:
            mcs.append(cons)  # UNSAT, causes conflict

    return mcs