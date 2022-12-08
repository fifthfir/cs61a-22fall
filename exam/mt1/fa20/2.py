def vote(vote):
    please = lambda nov: vote(nov) + third
    third = ty + 3
    return please
ty = 1
register = vote(lambda nov: nov + ty)
ty = 3
register(30)
