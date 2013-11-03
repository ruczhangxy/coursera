from orthogonalization import *
from math import sqrt

def norm(v):
    value = sum(v[k] ** 2 for k in v.D)
    return sqrt(value)

def orthonormalize(L):
    '''
    Input: a list L of linearly independent Vecs
    Output: A list T of orthonormal Vecs such that for all i in [1, len(L)],
            Span L[:i] == Span T[:i]
    '''
    ortho_list = orthogonalize(L)
    norm_list = [norm(v) for v in ortho_list]
    return [v / n for v, n in zip(ortho_list, norm_list)]


def adjust(v, factors):
    return Vec(v.D, {k:(v[k] * factors[k]) for k in v.D})

def aug_orthonormalize(L):
    '''
    Input:
        - L: a list of Vecs
    Output:
        - A pair Qlist, Rlist such that:
            * coldict2mat(L) == coldict2mat(Qlist) * coldict2mat(Rlist)
            * Qlist = orthonormalize(L)
    '''
    vstarlist, sigma_vecs = aug_orthogonalize(L)
    norm_list = [norm(v) for v in vstarlist]
    Qlist = [v / n for v, n in zip(vstarlist, norm_list)]
    Rlist = [adjust(v, norm_list) for v in sigma_vecs]

    return Qlist, Rlist

