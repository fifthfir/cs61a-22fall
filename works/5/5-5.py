def f(x):
    def g(y):
        if x == 1:
            return y
        else:
            return y + 9
    return g

print(f(5)(8))

def hol(f):
    def g(x):
        return f(x)
    return g

hol2 = lambda f: lambda x: f(x)