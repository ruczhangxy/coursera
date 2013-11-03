# version code 1049
# Please fill out this stencil and submit using the provided submission script.

from QR import factor
from orthogonalization import orthogonalize
from triangular import *
import orthonormalization
from mat import Mat
from matutil import *
from vec import Vec
from vecutil import list2vec
from matutil import listlist2mat



## Problem 1
def basis(vlist):
    '''
    Input:
        - vlist: a list of Vecs
    Output:
        - a list of linearly independent Vecs with equal span to vlist
    '''
    return [v for v in orthogonalize(vlist) if v * v > 10 ** -20]



## Problem 2
def subset_basis(vlist):
    '''
    Input:
        - vlist: a list of Vecs
    Output:
        - linearly independent subset of vlist with the same span as vlist
    '''
    orth_list = orthogonalize(vlist)
    return [v for i, v in enumerate(vlist) if orth_list[i] * orth_list[i] > 10 ** -20]



## Problem 3
def orthogonal_vec2rep(Q, b):
    '''
    Input:
        - Q: an orthogonal Mat
        - b: Vec whose domain equals the column-label set of Q.
    Output:
        - The coordinate representation of b in terms of the rows of Q.
    Example:
        >>> Q = Mat(({0, 1}, {0, 1}), {(0, 1): 0, (1, 0): 0, (0, 0): 2, (1, 1): 2})
        >>> b = Vec({0, 1},{0: 4, 1: 2})
        >>> orthogonal_vec2rep(Q, b) == Vec({0, 1},{0: 8, 1: 4})
        True
    '''
    return b * Q.transpose()



## Problem 4
def orthogonal_change_of_basis(A, B, a):
    '''
    Input:
        - A: an orthogonal Mat
        - B: an orthogonal Mat whose column labels are the row labels of A
        - a: the coordinate representation in terms of rows of A of some vector v 
    Output:
        - the Vec b such that b is the coordinate representation of v in terms of columns of B
    Example:
        >>> A = Mat(({0, 1, 2}, {0, 1, 2}), {(0, 1): 0, (1, 2): 0, (0, 0): 1, (2, 0): 0, (1, 0): 0, (2, 2): 1, (0, 2): 0, (2, 1): 0, (1, 1): 1})
        >>> B = Mat(({0, 1, 2}, {0, 1, 2}), {(0, 1): 0, (1, 2): 0, (0, 0): 2, (2, 0): 0, (1, 0): 0, (2, 2): 2, (0, 2): 0, (2, 1): 0, (1, 1): 2})
        >>> a = Vec({0, 1, 2},{0: 4, 1: 1, 2: 3})
        >>> orthogonal_change_of_basis(A, B, a) == Vec({0, 1, 2},{0: 8, 1: 2, 2: 6})
        True
    '''
    return a * A * B



## Problem 5
def orthonormal_projection_orthogonal(W, b):
    '''
    Input:
        - W: Mat whose rows are orthonormal
        - b: Vec whose labels are equal to W's column labels
    Output:
        - The projection of b orthogonal to W's row space.
    Example: 
        >>> W = Mat(({0, 1}, {0, 1, 2}), {(0, 1): 0, (1, 2): 0, (0, 0): 1, (1, 0): 0, (0, 2): 0, (1, 1): 1})
        >>> b = Vec({0, 1, 2},{0: 3, 1: 1, 2: 4})
        >>> orthonormal_projection_orthogonal(W, b) == Vec({0, 1, 2},{0: 0, 1: 0, 2: 4})
        True
    '''
    return b - W * b * W



## Problem 6
# Write your solution for this problem in orthonormalization.py.



## Problem 7
# Write your solution for this problem in orthonormalization.py.



## Problem 8
# Please give each solution as a Vec

least_squares_A1 = listlist2mat([[8, 1], [6, 2], [0, 6]])
least_squares_Q1 = listlist2mat([[.8,-0.099],[.6, 0.132],[0,0.986]])
least_squares_R1 = listlist2mat([[10,2],[0,6.08]]) 
least_squares_b1 = list2vec([10, 8, 6])

label_list = list(range(2))
bb = least_squares_b1 * least_squares_Q1
x_hat_1 = triangular_solve(mat2rowdict(least_squares_R1), label_list, bb)


least_squares_A2 = listlist2mat([[3, 1], [4, 1], [5, 1]])
least_squares_Q2 = listlist2mat([[.424, .808],[.566, .115],[.707, -.577]])
least_squares_R2 = listlist2mat([[7.07, 1.7],[0,.346]])
least_squares_b2 = list2vec([10,13,15])

bb = least_squares_b2 * least_squares_Q2
x_hat_2 = triangular_solve(mat2rowdict(least_squares_R2), label_list, bb)



## Problem 9
def QR_solve(A, b):
    '''
    Input:
        - A: a Mat
        - b: a Vec
    Output:
        - vector x that minimizes norm(b - A*x)
    Example:
        >>> domain = ({'a','b','c'},{'A','B'})
        >>> A = Mat(domain,{('a','A'):-1, ('a','B'):2,('b','A'):5, ('b','B'):3,('c','A'):1,('c','B'):-2})
        >>> Q, R = QR.factor(A)
        >>> b = Vec(domain[0], {'a': 1, 'b': -1})
        >>> x = QR_solve(A, b)
        >>> result = A.transpose()*(b-A*x)
        >>> result * result < 1E-10
        True
    '''
    Q, R = factor(A)
    bb = b * Q
    label_list = sorted(A.D[1], key=repr)
    sol = triangular_solve(mat2rowdict(R), label_list, bb)
    return sol

