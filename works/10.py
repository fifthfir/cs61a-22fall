def count(s, value):
    '''Count the number of times that...
    
    >>> count([1,2,1,2,1], 1)
    3
    '''
    total = 0
    for element in s:
        if element == value:
            total += 1
    return total

def sum_below(n):
    total = 0
    for i in range(n): # [0, 1, 2, ..., n]
        total += i
    return total

def cheer():
    for _ in range(3):
        print('Go bears!')

def mysum(L):
    '''
    >>> mysum([2, 4, 1, 5])
    12
    '''
    if L == []:
        return 0
    else:
        return L[0] + mysum(L[1:])

def sum_i(n):
    '''
    >>> sum_i(5)
    15
    '''
    total = 0
    for i in range(0, n+1):
        total += i
    return total

def sum_r(n):
    '''
    >>> sum_r(5)
    15
    '''
    if n == 0:
        return 0
    else:
        return n + sum_r(n - 1)

def divisors(n):
    return [1] + [x for x in range(2, n) if n % x == 0]

def reverse(word):
    '''
    >>> reverse('ShuYamino')
    'onimaYuhS'
    '''
    if len(word) == 1:
        return word
    else:
        return reverse(word[1:]) + word[0]



    

