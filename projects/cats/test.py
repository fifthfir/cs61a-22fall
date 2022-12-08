def shifty_shifts(start, goal, limit):
    '''
    >>> shifty_shifts("awful", "awesome", 3)
    5
    '''
    if limit < 0:
        return max(len(start), len(goal))
    if len(start) == 0 or len(goal) == 0:
        if start == goal:
            return 0
        else:
            return max(len(start), len(goal))
    else:
        if start[0] == goal[0]:
            step = 0
        else:
            step = 1
        return step + shifty_shifts(start[1:], goal[1:], limit - 1)