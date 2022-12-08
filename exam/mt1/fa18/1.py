identity = lambda x: x
increment = lambda x: x + 1

def fif(c, t, f, x):
    if c(x):
        return t(x)
    else:
        return f(x)

def bounce(x, y):
    while x < y:
        if x <= (y and x):
            print('a')
        if x > 0:
            print('b')
        elif x > -5:
            print('c')
        x, y = -y, increment(x - y)
        print(y)

crazy = lambda rich: 100 * rich
crazy = lambda rich: crazy(crazy(rich))

def ok(py):
    def h(w):
        print(py // 10)
        return ok(py)
    return lambda h: h(py)

def factorial(n):
    '''The factorial of positive n: n * (n-1) * (n-2) * ... * 1
    >>> factorial(4)
    24
    >>> factorial(1)
    1
    '''
    return n * fif(..., ..., ..., ...)