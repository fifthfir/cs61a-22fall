def wears_jacket_with_if(temp, raining):
    """
    >>> wears_jacket_with_if(90, False)
    False
    >>> wears_jacket_with_if(40, False)
    True
    >>> wears_jacket_with_if(100, True)
    True
    """
    return True if temp < 60 or raining == True else False

def is_prime(n):
    """
    >>> is_prime(10)
    False
    >>> is_prime(7)
    True
    """
    for i in range(2,n):
        if n % i != 0:
            return True
        else:
            return False
        
def double(x):
    return x * 2
hat = double
# double - function double[parent Global]
# hat - function double[parent Global]