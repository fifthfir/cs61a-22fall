'''
>>> x = 0
>>> abs(1/x if x != 0 else 0)
'''

def composel(f, g):
    def composed(x):
        return f(g(x))
    return composed
    # return lambda x: f(g(x))

def square(x):
    return x * x

def add_one(x):
    return x + 1

f = composel (square, add_one)
# f = composel(lambda x: x * x, lambda y: y + 1)

result = f(12)
print(result)