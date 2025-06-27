import numpy as np

e = 0 # value for empty cells
given = np.array([
    [8, e, e,  e, e, e,  e, e, e],
    [e, e, 3,  6, e, e,  e, e, e],
    [e, 7, e,  e, 9, e,  2, e, e],

    [e, 5, e,  e, e, 7,  e, e, e],
    [e, e, e,  e, 4, 5,  7, e, e],
    [e, e, e,  1, e, e,  e, 3, e],

    [e, e, 1,  e, e, e,  e, 6, 8],
    [e, e, 8,  5, e, e,  e, 1, e],
    [e, 9, e,  e, e, e,  4, e, e]])

import cpmpy as cp
#given = np.array(...)  # load the hints, uses '0' for the empty cells
grid = cp.intvar(1,9, shape=given.shape, name="grid")  # Decision variables
model = cp.Model(
    [cp.AllDifferent(row) for row in grid],
    [cp.AllDifferent(col) for col in grid.T],  # numpy's Transpose
    [cp.AllDifferent(grid[i:i+3, j:j+3]) \
        for i in range(0, 9, 3) for j in range(0, 9, 3)],
    grid[given!=0] == given[given!=0],  # enforce the hints
)
model.solve()

# Solve and print
if model.solve():
    print(model.status())
    #print(puzzle.value())
    # pretty print, mark givens with *
    out = ""
    for r in range(0,9):
        for c in range(0,9):
            out += str(grid[r,c].value())
            out += '* ' if given[r,c] else '  '
            if (c+1) % 3 == 0 and c != 8: # end of block
                out += '| '
        out += '\n'
        if (r+1) % 3 == 0 and r != 8: # end of block
            out += ('-'*9)+'+-'+('-'*9)+'+'+('-'*9)+'\n'
    print(out)
else:
    print("No solution found")
