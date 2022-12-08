def count(element, box):
    """Count how many times digit element appears in integer box.
    >>> count(2, 222122)
    5
    >>> count(0, -2020)
    2
    >>> count(0, 0) # 0 has no digits
    0
    """
    assert element >= 0 and element < 10
    box = abs(box)
    total = 0
    while box > 0:
        if element == box % 10:
            total += 1
        box = box // 10
    return total

def count_nine(element, box):
    """Count how many times digit element appears in the non-negative integer
    box in a place that is not next to a 9.
    >>> count_nine(2, 222122)
    5
    >>> count_nine(1, 1911191) # Only the middle 1 is not next to a 9
    1
    >>> count_nine(9, 9)
    1
    >>> count_nine(9, 99)
    0
    >>> count_nine(3, 314159265359)
    2
    >>> count_nine(5, 314159265359)
    1
    >>> count_nine(9, 314159265359)
    2
    >>> count_nine(0, 0) # No digits are in 0
    0
    """
    assert element >= 0 and element < 10
    assert box >= 0

    nine, total = False, 0
    while box > 0:
        if box % 10 == element and not (nine or box % 100 // 10 == 9):
            total = total + 1
        nine = box % 10 == 9
        box = box // 10
    return total

def fit(pegs, holes):
    """Return whether every digit in pegs appears at least as many times in
    holes as it does in pegs.
    >>> fit(123, 321) # Each digit appears once in pegs and in holes.
    True
    >>> fit(1213, 33221) # 1 appears twice in pegs, but only once in holes.
    False
    >>> fit(12, 22) # 1 appears once in pegs, but not at all in holes.
    False
    >>> fit(314159, 112233456789)
    True
    """
    i = 0
    while i <= 9:
        if count(i, pegs) > count(i, holes):
            return False
        i = i + 1
    return True