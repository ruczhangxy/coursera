import random
from GF2 import one
from vecutil import list2vec
from independence import is_independent
from itertools import combinations



## Problem 1
def randGF2(): return random.randint(0,1)*one
def flip(bit): return 0 if bit else one

a0 = list2vec([one, one,   0, one,   0, one])
b0 = list2vec([one, one,   0,   0,   0, one])

def randVec():
    return list2vec([randGF2() for i in range(6)])

def randVecList(n):
    return [randVec() for i in range(n)] 

def is_ok(U):
    vecs = [(U[i], U[i+1]) for i in range(0, len(U)-1, 2)]
    return all(is_independent(list(sum(x,()))) for x in combinations(vecs,min(len(vecs), 3)))

U = [a0, b0]
while len(U) < 10:
    new_vecs = randVecList(2)
    while not is_ok(U + new_vecs):
        new_vecs = randVecList(2)
    U += new_vecs
print(U)
