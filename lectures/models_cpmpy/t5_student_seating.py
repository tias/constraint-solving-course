import cpmpy as cp

n_chairs = 20
n_students = 15
n_tables = 5
n_programs = 3


model = cp.Model()

# Viewpoint 1
students = cp.intvar(1, n_chairs, shape=n_students)
model.add(cp.AllDifferent(students))

# Viewpoint 2
chairs = cp.intvar(0, n_students, shape=n_chairs)
model.add(cp.AllDifferentExceptN(chairs, 0))

