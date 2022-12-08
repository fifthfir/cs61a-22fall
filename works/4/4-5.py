def if_(c, t, f):
    if c:
        return t
    else:
        return f

from math import sqrt
def real_sqrt(x):
    if x > 0:
        return sqrt(x)
    else:
        return 0
    '''
    return if_(x > 0, sqrt(x), 0)
    will not work because of math domain error
    '''