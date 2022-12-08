def sequence(n, term):
    """Return the first n terms of a sequence as an integer.
    >>> sequence(6, abs) # Terms are 1, 2, 3, 4, 5, 6
    123456
    >>> sequence(5, lambda k: k+8) # Terms are 9, 10, 11, 12, 13
    910111213
    >>> sequence(4, lambda k: pow(10, k)) # Terms are 10, 100, 1000, 10000
    10100100010000
    """

    t, k = 0, 1
    while k <= n:
        m = 1
        x = term(k)
        while 10 * m <= x:
            m *= 10
        t = t * m * 10 + x
        k = k + 1
    return t