def sum_naturals(n):
    '''Sum the first Nnatural numbers
    
    >>> sum_naturals(5)
    15
    '''
    return summation(n, identity)

def sum_cubes(n):
    '''Sum the first n cubes of natural numbers
    
    >>> sum_cubes(5)
    225
    '''
    return summation(n, cube)

def summation(n, term):
    total, k = 0, 1
    while k <= n:
        total, k = total + term(k), k + 1
    return total

def identity(n):
    return n

def cube(n):
    return pow(n, 3)


