import numpy as np

# Data
n_jobs = 20
n_appls = 50
salary = np.random.randint(600, 1000, size=n_appls)
k = 4

# Model
import cpmpy as cp

# n_appls = ..., n_jobs = ..., salary = ..., k = ...
worker = cp.intvar(0, n_appls-1, shape=n_jobs)  # an applicant per job

model  = cp.Model(
           [cp.Count(worker, a) <= k for a in range(n_appls)]
         )

salary = cp.cpm_array(salary)  # make it indexible by variables
model.minimize(cp.sum([salary[worker[j]] for j in range(n_jobs)]))

model.solve()
print(worker.value())
