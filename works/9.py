def cascade(n):
    if n < 10:
        print(n)
    else:
        print(n)
        cascade(n//10)
        print(n)

def inverse_cascade(n):
    grow(n)
    print(n)
    shrink(n)

def f_then_g(f, g, n):
    if n:
        f(n)
        g(n)

grow = lambda n: f_then_g(grow, print, n // 10)
shrink = lambda n: f_then_g(print, shrink, n // 10)

def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fib(n-2) + fib(n-1)

def hanoi(n, start, end):
    other = 6 - start - end
    if n == 1:
        move(n, start, end)     
    else:
        hanoi(n-1, start, other)
        move(n, start, end)
        hanoi(n-1, other, end)

def move(n, where, to_go):
    print('Move disk ' + str(n) + ' from position ' + str(where) + ' to position ' + str(to_go) + '.')

def count_partitions(n, m):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    elif m == 0:
        return 0
    else:
        with_m = count_partitions(n-m, m)
        without_m = count_partitions(n, m-1)
        return with_m + without_m