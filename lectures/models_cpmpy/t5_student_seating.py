import cpmpy as cp
import numpy as np

n_chairs = 20
n_students = 15
n_tables = 5
n_programs = 3
tables = list(np.array_split(range(n_chairs), n_tables))

# Viewpoint 1
students = cp.intvar(0, n_chairs - 1, shape=n_students, name="students")
model1 = cp.Model(
    cp.AllDifferent(students),
    cp.all(
        (
            (cp.sum(students == chair for chair in table) == 0)
            | (cp.sum(students == chair for chair in table) >= 2)
        )
        for table in tables
    ),
)


# Viewpoint 2
chairs = cp.intvar(-1, n_students - 1, shape=n_chairs, name="chairs")
model2 = cp.Model(
    cp.AllDifferentExceptN(chairs, -1),
    cp.all(
        ((cp.sum(chairs[table] != -1) == 0) | (cp.sum(chairs[table] != -1) >= 2))
        for table in tables
    ),
    cp.all(cp.any(chairs == i) for i in range(n_students)),
)


assert model1.solve()
for student in students:
    print(f"{student} = {student.value()}")

assert model2.solve()
for chair in chairs:
    print(f"{chair} = {chair.value()}")


# Auxiliary variables
table_sums = [cp.sum(students == chair for chair in table) for table in tables]
model3 = cp.Model(
    cp.AllDifferent(students),
    cp.all(((t == 0) | (t >= 2)) for t in table_sums),
)
model3.add(cp.all(t <= 4 for t in table_sums))
assert model3.solve()
