from hw6 import *
from GF2 import one
from matutil import *

cols = ['A', 'B', 'C', 'D', 'E']
D = set(cols)
U_rows = [Vec(D,{'E': one, 'D': one, 'A': 0, 'C': 0, 'B': one}), Vec(D,{'E': 0, 'D': one, 'A': 0, 'C': 0, 'B': 0}), Vec(D,{'E': 0, 'D': 0, 'A': one, 'C': one, 'B': 0}), Vec(D,{'E': 0, 'D': 0, 'A': 0, 'C': 0, 'B': 0})]
b_list = [0, 0, one, 0]
print(rowdict2mat(U_rows))
print(echelon_solve(U_rows, cols, b_list))

U_rows=[Vec(D,{'E': one, 'D': one, 'A': one, 'C': one, 'B': one}), Vec(D,{'E': one, 'D': 0, 'A': 0, 'C': 0, 'B': one}), Vec(D,{'E': one, 'D': 0, 'A': 0, 'C': one, 'B': 0}), Vec(D,{'E': one, 'D': one, 'A': 0, 'C': 0, 'B': 0})]
b_list = [0, one, 0, one] 
print(rowdict2mat(U_rows))
print(echelon_solve(U_rows, cols, b_list))
