from vec import Vec
from mat import Mat
from matutil import *
from bitutil import *
from GF2 import *

## Task 1 part 1
""" Create an instance of Mat representing the generator matrix G. You can use
the procedure listlist2mat in the matutil module (be sure to import first).
Since we are working over GF (2), you should use the value one from the
GF2 module to represent 1"""
list_of_rows_G = [[one, 0, one, one],[one, one, 0, one],[0, 0, 0, one],[one, one, one, 0],[0, 0, one, 0],[0, one, 0, 0],[one, 0, 0, 0]]
G = listlist2mat(list_of_rows_G)

## Task 1 part 2
# Please write your answer as a list. Use one from GF2 and 0 as the elements.
encoding_1001 = [0,0,one,one,0,0,one]


## Task 2
# Express your answer as an instance of the Mat class.
'''
tmp = [[0,0,0,0,0,0,one],
       [0,0,0,0,0,one,0],
       [0,0,0,0,one,0,0],
       [0,0,one,0,0,0,0]]
R = listlist2mat(tmp)
'''
R = Mat((set(range(4)), set(range(7))), {(0,6):one, (1,5):one, (2,4):one, (3,2):one})

## Task 3
# Create an instance of Mat representing the check matrix H.
list_of_rows = [[0,0,0,one,one,one,one],
        [0,one,one,0,0,one,one],
        [one,0,one,0,one,0,one]]
H = listlist2mat(list_of_rows)

## Task 4 part 1
def find_error(e):
    """
    Input: an error syndrome as an instance of Vec
    Output: the corresponding error vector e
    Examples:
        >>> find_error(Vec({0,1,2}, {0:one}))
        Vec({0, 1, 2, 3, 4, 5, 6},{3: one})
        >>> find_error(Vec({0,1,2}, {2:one}))
        Vec({0, 1, 2, 3, 4, 5, 6},{0: one})
        >>> find_error(Vec({0,1,2}, {1:one, 2:one}))
        Vec({0, 1, 2, 3, 4, 5, 6},{2: one})    
    """
    cols = mat2coldict(H)
    D = set(range(7))
    for col, vec in cols.items():
        if vec == e:
            return Vec(D, {col:one})
    return Vec(D, {})

## Task 4 part 2
# Use the Vec class for your answers.
non_codeword = Vec({0,1,2,3,4,5,6}, {0: one, 1:0, 2:one, 3:one, 4:0, 5:one, 6:one})
error_vector = Vec({0,1,2,3,4,5,6}, {6:one})
code_word = Vec({0,1,2,3,4,5,6}, {0: one, 1:0, 2:one, 3:one, 4:0, 5:one, 6:0})
original = R * code_word # R * code_word


## Task 5
def find_error_matrix(S):
    """
    Input: a matrix S whose columns are error syndromes
    Output: a matrix whose cth column is the error corresponding to the cth column of S.
    Example:
        >>> S = listlist2mat([[0,one,one,one],[0,one,0,0],[0,0,0,one]])
        >>> find_error_matrix(S)
        Mat(({0, 1, 2, 3, 4, 5, 6}, {0, 1, 2, 3}), {(1, 2): 0, (3, 2): one, (0, 0): 0, (4, 3): one, (3, 0): 0, (6, 0): 0, (2, 1): 0, (6, 2): 0, (2, 3): 0, (5, 1): one, (4, 2): 0, (1, 0): 0, (0, 3): 0, (4, 0): 0, (0, 1): 0, (3, 3): 0, (4, 1): 0, (6, 1): 0, (3, 1): 0, (1, 1): 0, (6, 3): 0, (2, 0): 0, (5, 0): 0, (2, 2): 0, (1, 3): 0, (5, 3): 0, (5, 2): 0, (0, 2): 0})
    """
    input_cols = mat2coldict(S)
    output_cols = {key:find_error(value) for key, value in input_cols.items()}
    return coldict2mat(output_cols)

## Task 6
s = "I'm trying to free your mind, Neo. But I can only show you the door. You’re the one that has to walk through it."
b = str2bits(s)
P = bits2mat(b)

## Task 7
C = G * P
bits_before = len(P.D[0]) * len(P.D[1])
bits_after = len(C.D[0]) * len(C.D[1])


## Ungraded Task
CTILDE = None

## Task 8
def correct(A):
    """
    Input: a matrix A each column of which differs from a codeword in at most one bit
    Output: a matrix whose columns are the corresponding valid codewords.
    Example:
        >>> A = Mat(({0,1,2,3,4,5,6}, {1,2,3}), {(0,3):one, (2, 1): one, (5, 2):one, (5,3):one, (0,2): one})
        >>> correct(A)
        Mat(({0, 1, 2, 3, 4, 5, 6}, {1, 2, 3}), {(0, 1): 0, (1, 2): 0, (3, 2): 0, (1, 3): 0, (3, 3): 0, (5, 2): one, (6, 1): 0, (3, 1): 0, (2, 1): 0, (0, 2): one, (6, 3): one, (4, 2): 0, (6, 2): one, (2, 3): 0, (4, 3): 0, (2, 2): 0, (5, 1): 0, (0, 3): one, (4, 1): 0, (1, 1): 0, (5, 3): one})
    """
    return A + find_error_matrix(H*A)
