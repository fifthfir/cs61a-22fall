def growth(baseline):
    '''Return a function that can be called repeatedly on numbers and prints
    the difference between its argument and the smallest argument used so far
    (including baseline).

    >>> job = growth(148)(149)(150)(130)(133)(139)(137)
    1
    2
    0
    3
    9
    7
    '''
    def increase(observed):
        under = min(baseline, observed)
        print(observed - under)
        return growth(under)
    return increase

def square(x):
    return x * x

def maxer(smoke):
    '''Return a repeatable function fire(y) that prints the largest smoke(y) so far.
    
    >>> h = maxer(square)(2)(1)(3)(2)(-4) # print the largest square(y) so far
    4
    4
    9
    9
    16
    >>> h = maxer(abs)(2)(1)(3)(2)(-4) # print the largest abs(y) so far
    2
    2
    3
    3
    4
    '''
    def fire(y):
        print(smoke(y))
        def haze(z):
            if smoke(y) > smoke(z):
                z = y
            return fire(z)
        return haze
    return fire