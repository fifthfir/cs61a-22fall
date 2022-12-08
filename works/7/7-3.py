def trace1(fn):
    def traced(x):
        print('Calling', fn, 'on argument', x)
        return fn(x)
    return traced

@trace1
def square(x):
    return x * x
# square = trace1(square)

@trace1
def sum_square_up_to(x):
    k = 1
    total = 0
    while k <= x:
        total, k = total + square(k), k + 1
    return total