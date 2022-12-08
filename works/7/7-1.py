def flip(flop):
    if flop == 3:
        return None
    flip = lambda flip: 3
    return flip

def flop(flip):
    return flop

flip, flop = flop, flip

flip(flop(1)(2))(3)