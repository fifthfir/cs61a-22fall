def search(f):
    '''找到让f(x)为True的x'''
    x = 0
    while True:
        if f(x):
            return x
        x += 1

def is_4_squared(x):
    return square(4) == x

def is_sqrt_of_16(x):
    return square(x) == 16

def sqrt(y):
    def is_sqrt_of_y(x):
        return square(x) == y        
    return search(is_sqrt_of_y)

def square(x):
    return x * x

def positive(x):
    '''A function that is 0 ubtil square(x)-100 is positive
    
    >>> search(positive)
    11
    '''
    return max(0, square(x) - 100)

def inverse(f):
    '''return g(y) such that g(f(x)) = x.
    
    >>> sqrt = inverse(square)
    >>> sqrt(16)
    4
    '''
    return lambda y: search(lambda x: f(x) == y)
    '''现有f, y, search找到让 f(x) == y 为True的x
    从而使这个 g (= inverse(f)) 可以输入y后得到x
    searchxxxx: 一个关于y的函数, 结果为x
    inverse(f)(y) = x'''

def inverse2(f):
    '''
    >>> inverse2(square)(4)
    2
    '''
    def inverse_f(y):
        def is_inverse_of_y(x):
            return f(x) == y
        return search(is_inverse_of_y)
    return inverse_f

def inverse_f(f):
    def h(y):
        g = lambda x: f(x) == y
        return search(g)
    return h

print(inverse_f(square)(25))

def f(x):
    return x + 1
g = lambda x: f
# g = lambda x: lambda y: y + 1
eight = g(2)(7)# 2 is ignored

h = lambda x: 9
print(h(0))