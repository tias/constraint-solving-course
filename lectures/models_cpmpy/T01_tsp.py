import cpmpy as cp

n_cities = 4;
distance = cp.cpm_array([
    [0,    85, 162, 231],   # Km from AMS
    [85,    0,  98, 128],   # Km from BRU
    [162,  98,   0, 146],   # Km from LUX
    [231, 128, 146, 0  ]    # Km from CDG
])
# Travel from c to Next[c]
Next = cp.intvar(0, n_cities-1, shape=n_cities)

# Successor variables must from a circuit
model = cp.Model( cp.Circuit(Next) )

model.minimize(cp.sum(distance[c, Next[c]] for c in range(n_cities)))

model.solve()
print(model.status())

print("Total Cost of solution", model.objective_value())
def display(sol):
    x = 0
    msg = "0"
    while sol[x] != 0:
        x = sol[x]
        msg += f" --> {x}"
    print(msg + " --> 0")
display(Next.value())
