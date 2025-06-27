import cpmpy as cp
import numpy as np

A = [["00","01"],
     ["10","11"]]
print(A[0][1])  # out: '01'

B = np.array(A)
print(B[0,1])  # out: '01'

print(B[0,:])  # out: ['00' '01']

Sel = [[False, True],
       [True, False]]
print(B[Sel])  # out: ['01' '10']

