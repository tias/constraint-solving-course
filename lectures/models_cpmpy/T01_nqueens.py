import cpmpy as cp

n = 8  # dimension of square board

# `q[i] == j` denotes that the queen in row `i` is in col `j`
q = cp.intvar(0, n - 1, shape=n, name="q")

# Constraints on columns, and on both diagonals
model = cp.Model(
    cp.AllDifferent(q),
    cp.AllDifferent([q[i] - i for i in range(n)]),
    cp.AllDifferent([q[i] + i for i in range(n)]),
)
model.solve()
print(q.value())  # [0 4 7 5 2 6 1 3]
exit(0)

# orig
# q[0] == 0,
# q[1] == 4
# flip
# 0 4 7 5 2 6 1 3
# q[0] == 7,
# q[3] == 0,
# 7 1 3 0 6 4 2 5
# rot
# q[7] == 7,
# q[0] == 5,
# q[1] == 3,
# 5 3 6 0 2 4 1 7


def show_sol():
    return
    for i in range(n):  # pretty print
        print(" ".join("Q" if q[i].value() == j else "." for j in range(n)))

    print(" ".join(str(q.value()) for q in q))
    print(
        ",".join(
            f"Q{('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')[j]}{8 - i}"
            for i in range(n)
            for j in range(n)
            if q[i].value() == j
        )
    )


# n_sols = model.solveAll(display=show_sol)
# print(f"Number of solutions: {n_sols}")


print(f"{n=}")
model.solve(
    solver="ortools", symmetry_level=0, symmetry_detection_deterministic_time_limit=0
)
# model.solve(solver="pumpkin")
print(f"{model.status()}")
model += q[0] <= (n // 2) - 1
# n_sols = model.solveAll(display=show_sol)
# print(f"Number of solutions: {n_sols}")
model.solve(
    solver="ortools", symmetry_level=0, symmetry_detection_deterministic_time_limit=0
)
# model.solve(solver="pumpkin")
print(f"{model.status()}")

exit(0)
model.solve(solver="minizinc:gecode")
print(f"{model.status()}")
model += q[0] <= (n // 2) - 1
model.solve(solver="minizinc:gecode")
print(f"{model.status()}")
