def run_checker(condition, result):
    """
    Returns a chain function. Each call in a chain that starts with
    this returned function prints "No run!" if CONDITION returns a false
    value when applied to the previous two arguments and the current argument,
    and otherwise prints the result of applying RESULT to these same
    three arguments. For calls in the chain where there are fewer than two
    preceding calls in the chain, the missing arguments are taken to be -1.
    >>> f = run_checker(lambda a, b, c: a > b > c and a >= 10, lambda a, b, c: a*(b+c))
    >>> f = f(15)
    No run!
    >>> f = f(10)
    No run!
    >>> f = f(5)
    225
    >>> f = f(2)
    70
    >>> f = f(1)
    No run!
    >>> f = f(11)
    No run!
    >>> f = f(12)
    No run! 
    >>> f = f(10)
    No run!
    >>> f = f(2)
    144
    """
    def f(x, y):
        def g(n):
            if condition(x, y, n):
                print(result(x, y, n))
            else:
                print('No run!')
            return f(y, n)
        return g
    return f(-1, -1) # So difficult