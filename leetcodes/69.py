def sqrt(x):
    l, r = 0, x
    while l <= r:
        m = (l + r) // 2
        if m ** 2 <= x <= (m + 1) ** 2:
            return m
        elif x < m ** 2:
            r = m - 1 # why
        else:
            l = m + 1 # why
print(sqrt(25))    