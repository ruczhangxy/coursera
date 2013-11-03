from vec import Vec
from itertools import product

def getitem(M, k):
    "Returns the value of entry k in M.  The value of k should be a pair."
    assert k[0] in M.D[0] and k[1] in M.D[1]
    return M.f.get(k, 0)

def setitem(M, k, val):
    "Sets the element of v with label k to be val.  The value of k should be a pair"
    assert k[0] in M.D[0] and k[1] in M.D[1]
    M.f[k] = val

def add(A, B):
    "Returns the sum of A and B"
    assert A.D == B.D
    return Mat(A.D, {(x, y): (A[(x, y)] + B[(x, y)]) for x, y in product(A.D[0], A.D[1])})

def scalar_mul(M, alpha):
    "Returns the product of scalar alpha with M" 
    f = {key:(value * alpha) for key, value in M.f.items()}
    return Mat(M.D, f)

def equal(A, B):
    "Returns true iff A is equal to B"
    assert A.D == B.D
    return all(A[(x, y)] == B[(x, y)] for x, y in product(A.D[0], A.D[1]))

def transpose(M):
    "Returns the transpose of M"
    return Mat((M.D[1], M.D[0]), {(key[1], key[0]): value for key, value in M.f.items()})

def mat2rowdict(A):
  '''
  Copied from matutil.py
  '''
  return {row:Vec(A.D[1], {col:A[row,col] for col in A.D[1]}) for row in A.D[0]}

def vector_matrix_mul(v, M):
    "Returns the product of vector v and matrix M"
    assert M.D[0] == v.D
    row_dict = mat2rowdict(M)
    return sum(v[k] * row for k, row in row_dict.items())

def mat2coldict(A):
    '''
    Copied from matutil.py
    '''
    return {col:Vec(A.D[0], {row:A[row,col] for row in A.D[0]}) for col in A.D[1]}

def matrix_vector_mul(M, v):
    "Returns the product of matrix M and vector v"
    assert M.D[1] == v.D
    col_dict = mat2coldict(M)
    return sum(v[k] * col for k, col in col_dict.items())

def keys(d):
    '''
    Copied from matutil.py
    '''
    return d.keys() if isinstance(d, dict) else range(len(d))

def value(d):
    '''
    Copied from matutil.py
    '''
    return next(iter(d.values())) if isinstance(d, dict) else d[0]

def rowdict2mat(rowdict):
    '''
    Copied from matutil.py
    '''
    col_labels = value(rowdict).D
    return Mat((set(keys(rowdict)), col_labels), {(r,c):rowdict[r][c] for r in keys(rowdict) for c in col_labels})

def matrix_matrix_mul(A, B):
    "Returns the product of A and B"
    assert A.D[1] == B.D[0]
    row_dict_A = mat2rowdict(A)
    target_row_dict = {key : row * B for key, row in row_dict_A.items()}
    return rowdict2mat(target_row_dict)

################################################################################

class Mat:
    def __init__(self, labels, function):
        self.D = labels
        self.f = function

    __getitem__ = getitem
    __setitem__ = setitem
    transpose = transpose

    def __neg__(self):
        return (-1)*self

    def __mul__(self,other):
        if Mat == type(other):
            return matrix_matrix_mul(self,other)
        elif Vec == type(other):
            return matrix_vector_mul(self,other)
        else:
            return scalar_mul(self,other)
            #this will only be used if other is scalar (or not-supported). mat and vec both have __mul__ implemented

    def __rmul__(self, other):
        if Vec == type(other):
            return vector_matrix_mul(other, self)
        else:  # Assume scalar
            return scalar_mul(self, other)

    __add__ = add

    def __sub__(a,b):
        return a+(-b)

    __eq__ = equal

    def copy(self):
        return Mat(self.D, self.f.copy())

    def __str__(M, rows=None, cols=None):
        "string representation for print()"
        if rows == None:
            try:
                rows = sorted(M.D[0])
            except TypeError:
                rows = sorted(M.D[0], key=hash)
        if cols == None:
            try:
                cols = sorted(M.D[1])
            except TypeError:
                cols = sorted(M.D[1], key=hash)
        separator = ' | '
        numdec = 3
        pre = 1+max([len(str(r)) for r in rows])
        colw = {col:(1+max([len(str(col))] + [len('{0:.{1}G}'.format(M[row,col],numdec)) if isinstance(M[row,col], int) or isinstance(M[row,col], float) else len(str(M[row,col])) for row in rows])) for col in cols}
        s1 = ' '*(1+ pre + len(separator))
        s2 = ''.join(['{0:>{1}}'.format(c,colw[c]) for c in cols])
        s3 = ' '*(pre+len(separator)) + '-'*(sum(list(colw.values())) + 1)
        s4 = ''.join(['{0:>{1}} {2}'.format(r, pre,separator)+''.join(['{0:>{1}.{2}G}'.format(M[r,c],colw[c],numdec) if isinstance(M[r,c], int) or isinstance(M[r,c], float) else '{0:>{1}}'.format(M[r,c], colw[c]) for c in cols])+'\n' for r in rows])
        return '\n' + s1 + s2 + '\n' + s3 + '\n' + s4

    def pp(self, rows, cols):
        print(self.__str__(rows, cols))

    def __repr__(self):
        "evaluatable representation"
        return "Mat(" + str(self.D) +", " + str(self.f) + ")"
