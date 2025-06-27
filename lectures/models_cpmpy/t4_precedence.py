import cpmpy as cp

D = [2,1,4,2,3,1,0] # Durations

S = cp.intvar(1, sum(D), shape=7)
model = cp.Model()

model.add([S[0]+D[0] <= S[1], S[0]+D[0] <= S[2],
           S[0]+D[0] <= S[3], S[1]+D[1] <= S[4],
           S[2]+D[2] <= S[5], S[3]+D[3] <= S[4],
           S[4]+D[4] <= S[6], S[5]+D[5] <= S[6]])

model.minimize(S[6])

model.solve()
