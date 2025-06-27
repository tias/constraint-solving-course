import cpmpy as cp

x = cp.intvar(0,5,shape=(2,2))
con = sum(x)
print(con)
