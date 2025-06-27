import cpmpy as cp
import numpy as np

# Parameters
Apps = 5  # Example number of applicants (you can set this to any value)
Jobs = 3  # Example number of jobs (you can set this to any value)

# Salary for each applicant
Salary = np.array([500, 600, 700, 800, 900])

# Decision variables: worker[j] is the applicant assigned to job j
workers = cp.intvar(0, Apps-1, shape=Jobs)  # Worker[j] is in the range of applicants

# Define the model
model = cp.Model()

# Objective: Minimize the total salary cost for assigned jobs
Salary = cp.cpm_array(Salary) # convert into a cpmpy-compatible array
total_cost = cp.sum([Salary[worker] for worker in workers])
model.minimize(total_cost)

# Example constraints: Qualifications, workload, etc.

# Example constraint: Worker 0 can't be assigned to job 1
model.add(workers[1] != 0)
# Example constraint: Ensure no duplicate assignments (each worker can only be assigned to one job)
model.add(cp.AllDifferent(workers))

# Solve the model
if model.solve():
    print("Optimal Assignment:", workers.value())
    print("Total Salary Cost:", total_cost.value())
else:
    print("No solution found")
