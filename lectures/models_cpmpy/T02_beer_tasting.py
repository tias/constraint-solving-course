import cpmpy as cp
m = cp.Model()

st,du,vi,tk,gc,kl = cp.boolvar(shape=6)

m.add(52*st + 85*du + 60*vi + 84*tk + 117*gc + 35*kl <= 4*52)

m.maximize(50*st + 80*du + 75*vi + 82*tk + 95*gc + 70*kl)      
      
      
m.solve()


print(m.status())
print(f"Stella: {st.value()}")
print(f"Duvel: {du.value()}")
print(f"Vedette IPA: {vi.value()}")
print(f"Triple Karmeliet: {tk.value()}")
print(f"Gouden Carolus Whiskey Infused: {gc.value()}")
print(f"Kriek Lindemans: {kl.value()}")
