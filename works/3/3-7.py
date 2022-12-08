def fib(n):
    '''fibxxxx
    
    >>> fib(8)
    13
    >>> fib(16)
    610
    '''
    pre = 0
    cur = 1
    k = 2
    while k < n:
        pre, cur = cur, pre+cur
        k += 1
    return cur
    '''
    from doctest import testmod
    testmod()
    '''