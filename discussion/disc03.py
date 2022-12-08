def multiply(m, n):
    '''
    >>> multiply(5, 3)
    15
    '''
    if n == 1:
        return m
    else:
        return m + multiply(m, n-1)

def hailstone(n):
    '''Print out the hailstone sequence starting at n, and return
    the number of elements in the sequence.
    
    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    '''
    if n == 1:
        print(n)
        return 1
    elif n % 2 == 0:
        print(n)
        m = n // 2
    else:
        print(n)
        m = n * 3 + 1
    return hailstone(m) + 1

def merge(n1, n2):
    '''Merge two numbers.
    >>> merge(31, 42)
    4321
    >>> merge(21, 0)
    21
    >>> merge(21, 31)
    3211
    '''
    if n1 == 0 or n2 == 0:
        return max(n1, n2)
    else:
        last1, save1 = n1 % 10, n1 // 10
        last2, save2 = n2 % 10, n2 // 10
        if last1 <= last2:
            last = last1
            n1 = save1
        else:
            last = last2
            n2 = save2
        return last + 10 * merge(n1, n2)

def make_func_repeater(f, x):
    '''
    >>> incr_1 = make_func_repeater(lambda x: x + 1, 1)
    >>> incr_1(2) # same as f(f(x))
    3
    >>> incr_1(5)
    6
    '''

    def repeat(n):
        if n == 1:
            return f(x)
        else:
            return f(repeat(n-1))
    return repeat

def is_prime(n):
    '''
    >>> is_prime(7)
    True
    >>> is_prime(10)
    False
    >>> is_prime(1)
    False
    '''
    def prime_helper(k):
        if k == n:
            return True
        elif n % k == 0 or n == 1:
            return False
        else:
            return prime_helper(k+1)
    return prime_helper(2)