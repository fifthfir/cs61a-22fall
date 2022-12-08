from operator import floordiv, mod
from re import I

def divide_exact(n, d = 10):
    '''return the quotient and reminder of dividing n by d.
    
    >>> a,b = divide_exact(2022,2)
    >>> a
    1011
    >>> b
    0
    '''
    # python -m doctest xx.py -v
    return floordiv(n,d), mod(n,d)

def absolute_value(x):
    if x < 0 :
        return -x
    elif x == 0:
        return 0
    else:
        return x

i, total = 0, 0
while i < 874:
    i += 1
    total += i
print(i, total)
