import numpy as np

# Data
n_jobs = 20
n_apps = 50
salary = np.random.randint(600, 1000, size=n_apps)

# Model
import cpmpy as cp

# n_apps = ..., n_jobs = ..., salary = ...
worker = cp.intvar(0, n_apps-1, shape=n_jobs)  # an applicant per job

model  = cp.Model(
            # qualifications, workload, etc
         )

salary = cp.cpm_array(salary)  # make it indexible by variables
model.minimize(cp.sum([salary[worker[j]] for j in range(n_jobs)]))

model.solve()
print(worker.value())
