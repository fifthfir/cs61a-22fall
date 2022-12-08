def make_adder(n):
    return lambda k: n + k

from operator import add

def curry2(f):
    def h(x):
        def g(y):
            return f(x,y)
        return g
    return h

curry3 = lambda f: lambda x:lambda y: f(x, y)

curried_pow = curry2(pow)
two_to_the = curried_pow(2)
x = two_to_the(5)

def two_to_the(y):
    return pow(2, y)

two_to_the = curry2(pow)(2)

