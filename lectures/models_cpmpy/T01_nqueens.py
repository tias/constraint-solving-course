import cpmpy as cp

N = 8  # dimension of square board

# Variables (one per row, indicating the column position)
Row = cp.intvar(1,N, shape=N, name="Row")

# Constraints on columns and main/anti diagonals
model = cp.Model([
    cp.AllDifferent(Row),
    cp.AllDifferent([Row[i] - i for i in range(N)]),
    cp.AllDifferent([Row[i] + i for i in range(N)]),
])
model.solve()
    
for C in Row.value():  # pretty print
    print(" ".join('Q' if j == C else '.' for j in range(N)))
