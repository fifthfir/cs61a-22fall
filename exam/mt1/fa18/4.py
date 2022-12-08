def rect(area, perimeter):
    """Return the longest side of a rectangle with area and perimeter that has integer sides.
    >>> rect(10, 14) # A 2 x 5 rectangle
    5
    >>> rect(5, 12) # A 1 x 5 rectangle
    5
    >>> rect(25, 20) # A 5 x 5 rectangle
    5
    >>> rect(25, 25) # A 2.5 x 10 rectangle doesn't count because sides are not integers
    False
    >>> rect(25, 29) # A 2 x 12.5 rectangle doesn't count because sides are not integers
    False
    >>> rect(100, 50) # A 5 x 20 rectangle
    20
    """
    side = 1
    while side * side <= area:
        other = round(0.5 * perimeter - side)
        if side * other == area and 2 * (side + other) == perimeter:
            return other # the longest side
        side = side + 1
    return False