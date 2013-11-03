# Please fill out this stencil and submit using the provided submission script.





## Problem 1
def myFilter(L, num): return [n for n in L if n % num != 0]



## Problem 2
def myLists(L): return [list(range(1, x+1)) for x in L]



## Problem 3
def myFunctionComposition(f, g):
    return {x:g[f[x]] for x in f}


## Problem 4
# Please only enter your numerical solution.

complex_addition_a = 5 + 3j
complex_addition_b = 1j
complex_addition_c = -1 + 0.001j
complex_addition_d = 0.001 + 9j



## Problem 5
GF2_sum_1 = 1
GF2_sum_2 = 0
GF2_sum_3 = 0


## Problem 6
def mySum(L):
    total = 0
    for x in L:
        total += x
    return total



## Problem 7
def myProduct(L):
    total = 1
    for x in L:
        total *= x
    return total



## Problem 8
def myMin(L):
    m = L[0]
    for x in L:
        if x < m:
            m = x
    return m



## Problem 9
def myConcat(L):
    ret = ''
    for s in L:
        ret += s
    return ret



## Problem 10
def myUnion(L):
    ret = set()
    for s in L:
        ret |= s
    return ret

