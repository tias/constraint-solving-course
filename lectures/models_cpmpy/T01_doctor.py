import numpy as np

# Data
n_days = 7; n_doctors = 5
n_shifts = 4; Appt, Call, Oper, Free = range(n_shifts)

# Model
import cpmpy as cp
roster = cp.intvar(0,n_shifts-1, shape=(n_doctors,n_days))
model  = cp.Model(
    # on-call/day = 1
    [cp.Count(roster[:,d], Call) == 1 for d in range(n_days)],
    # oper/weekday <= 2; assume d mod 7 == 0 for Monday, etc
    [cp.Count(roster[:,d], Oper) <= 2 for d in range(n_days) if d % 7 <= 4],
    # oper/week >= 7
    [cp.Count(roster[:,s:s+7], Oper) >= 7 for s in range(0, n_days, 7)],
    # appt/week >= 4
    [cp.Count(roster[:,s:s+7], Appt) >= 4 for s in range(0, n_days, 7)],
    # free after oper
    [(roster[p,d] == Oper).implies(roster[p,d+1] == Free) for p in range(n_doctors) for d in range(n_days-1)],
)
# maximize nr of free shifts in weekend
model.maximize(cp.sum([cp.Count(roster[:,s+5:s+7], Free) for s in range(0, n_days, 7)]))
model.solve()


# Pretty printing
shift_map = {Appt: 'A', Call: 'C', Oper: 'O', Free: 'F'}
mapped = np.array([[shift_map[val] for val in row] for row in roster.value()])
print(mapped)
