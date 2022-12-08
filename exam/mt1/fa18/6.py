def repeat(k):
    """When called repeatedly, print each repeated argument.
    >>> f = repeat(1)(7)(7)(3)(4)(2)(5)(1)(6)(5)(1)
    7
    1
    5
    1
    """
    return detector(lambda j: False)(k)

def detector(have_seen):
    def g(i):
        if have_seen(i):
            print(i)
        return detector(lambda j: j == i or have_seen(j)) # the iteration of have_seen_i_before
    return g