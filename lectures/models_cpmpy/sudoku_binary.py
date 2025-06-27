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
from cpmpy.expressions.utils import all_pairs
#given = np.array(...)  # load the hints
grid = cp.intvar(1,9, shape=given.shape, name="grid")  # Decision variables

model = cp.Model(
    grid[given!=0] == given[given!=0],  # enforce the hints
    [[cell1 != cell2 for cell1, cell2 in all_pairs(row)]
     for row in grid],
    [[cell1 != cell2 for cell1, cell2 in all_pairs(col)]
     for col in grid.T],
    [[cell1 != cell2 for cell1, cell2
      in all_pairs(grid[i:i+3, j:j+3].flat)]
     for i in [0, 3, 6] for j in [0, 3, 6]]
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
