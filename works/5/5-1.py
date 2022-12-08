def apply_twice(f, x):
    return f(f(x))

def square(x):
    return x * x

def repeat(f,x):
    while f(x) != x: # 这个f(x)每次都不一样噢
        x = f(x)
    return x

def g(y):
    return (y + 5) // 3

def f(x, y):
    return g(x)

# def g(x):
    # return x + y # parent = Global. environment: g & Global. not defined y

def triple(x):
    return 3 * x

def compose1(f, g):
    def h(x):
        return f(g(x))
    return h

def make_adder(x):
    def adder(n):
        return n + x
    return adder

compose1(square, make_adder(2))(3)