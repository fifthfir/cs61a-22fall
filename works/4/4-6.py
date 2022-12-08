from math import sqrt

def has_big_sqrt(x):
    return x > 0 and sqrt(x) > 10
has_big_sqrt(-1000)#will not crash cuz it returns right

def reasonable(n):
    '''
    >>> reasonable(0)
    True
    >>> reasonable(100)
    True
    >>> reasonalble(10 ** 1000)
    False
    
    1 will not crash cuz it returns left
    3因为太小了直接约成0'''
    return n == 0 or 1 / n != 0