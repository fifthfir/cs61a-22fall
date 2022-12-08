def print_all(x):
    print(x)
    return print_all
print_all(1)(2)(3)

def print_sums(x):
    print(x)
    def next_sum(y):
        return print_sums(x + y)
    return next_sum
print_sums(1)(3)(5)

g = print_sums(1)
h = g(3)
w = h(5)