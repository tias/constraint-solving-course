import numpy as np

import cpmpy as cp

grid = cp.intvar(1,9, shape=(9,9), name="grid")  # Decision variables
model = cp.Model(
    [cp.AllDifferent(row) for row in grid],
    [cp.AllDifferent(col) for col in grid.T],  # numpy's Transpose
    [cp.AllDifferent(grid[i:i+3, j:j+3]) \
        for i in range(0, 9, 3) for j in range(0, 9, 3)]
)

# solve with default solver: ortools
model.solve()

solutions = 0  # initialize
solution_limit = 5  # find 5 solutions

# model.solve() returns true if a solution is found
while model.solve() and solutions < solution_limit:
    solutions += 1
    # Constraint to enforce different solution
    model.add(~cp.all(grid == grid.value()))
    # The above is equivalent to
    model.add(cp.any(cell != cell.value() for cell in grid.flatten()))  # flatten grid, otherwise you get just the rows
