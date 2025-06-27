import cpmpy as cp

IV = cp.intvar(-2,5)
BV = cp.boolvar()
model = cp.Model()

model.add(IV != 3)
model.add(BV == True)
model.add(5 % IV > 2)

#model.solve()

try:
    # The last constraint printed before the exception is the issue
    for c in model.constraints:
        print("Trying",c)
        cp.Model(c).solve()
except:
    print(f"constraint {c} is bugged")