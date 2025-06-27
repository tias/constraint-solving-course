import cpmpy as cp
import numpy as np
m = cp.Model()

(a,b,c) = cp.boolvar(shape=3)
m.add(a | b)  # a OR b
m.add(~(a & b))  # NOT (a AND b)
m.add(a.implies(b | c))  # a -> (b OR c)
m.add(a == b)  # equivalence: (a -> b) & (b -> a)
m.add(a != b)  # same as ~(a==b) and same as (a == ~b)

Bv = cp.boolvar(shape=3)
m.add(cp.any([Bv[0], Bv[1], Bv[2]]))  # explicit list
m.add(~cp.all(Bv))  # (numpy) array


b = cp.boolvar()
x = cp.intvar(0, 10)
Iv = cp.intvar(0, 10, shape=3)

m.add(x > 3)
m.add(x != 6)

m.add(Iv == 1)  # vectorized, shorthand for:
m.add([Iv[0] == 1, Iv[1] == 1, Iv[2] == 1])


Xs = cp.intvar(0, 10, shape=3, name="Xs")
Ys = cp.intvar(1, 10, shape=3, name="Ys")
W = np.array([1,3,-5])  # numpy array for use in vectorized multiplication

m.add(Xs[0] - Ys[0] == 5)
m.add(cp.sum(Xs) != 1)
m.add(cp.sum(W*Xs) > 3)  # 1*Xs[0] + 3*Xs[1] + (-5)*Xs[2] > 3

# arbitrary nested expressions:
m.add(3*Xs[0] < abs(5 - cp.max(Xs) + cp.min(Ys)))


Ivs = cp.intvar(1,10, shape=4, name="ivs")
b = cp.boolvar()

m.add(cp.AllDifferent(Ivs))
m.add(b.implies(cp.AllEqual(Ivs)))
m.add(cp.max(Ivs) == 3)  # maximum of 'ivs' values equals 3
m.add(cp.Table(Ivs, [[1,1,2,4],  # values must match one of the rows
                     [1,2,3,6],
                     [2,3,5,10]]))

# skip:
m.add(cp.Count(Ivs, 2) > 1)  # number of 'ivs' values that equal 2, is larger than 1

# see later in course?
idxvar = cp.intvar(0,len(Ivs)-1)  # indexing is offset 0
m.add(Ivs[idxvar] == 2)  # variable at index 'idxvar's value, must equal 2
