import cpmpy as cp
from cpmpy.expressions.utils import all_pairs

varieties,blocks = 7,7
sampleSize,blockSize = 3,3
balance = 1

BIBD = cp.boolvar(shape=(varieties, blocks),name="matrix")

model = cp.Model(
    # every row must add up to sampleSize
    [cp.sum(row) == sampleSize for row in BIBD], 
    # every column must add up to blocksize
    [cp.sum(col) == blockSize for col in BIBD.T], 
    # the scalar product of every pair of distinct rows must sum up to balance
    [cp.sum(row_i*row_j) == balance for row_i, row_j in all_pairs(BIBD)]
)

model.solve()

# in lecture: print the first constraint
print("The first (list of) constraint:",[cp.sum(row) == sampleSize for row in BIBD])


if model.solve():
    # pretty print
    print(f"BIBD: {varieties} obj, {blocks} blocks, sampleSize={sampleSize}, blockSize={blockSize}, balance={balance}")
    for (i,row) in enumerate(BIBD.value()):
        srow = "".join('X ' if e else '  ' for e in row)
        print(f"Object {i+1}: [ {srow}]")
else:
    print("No solution found")
