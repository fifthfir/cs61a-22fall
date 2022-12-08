from operator import mul
radius = 5
def square():
    return mul(radius,radius)
radius *= 9
print(square())
# argument 实参 parameter 形参
# built-in function / user defined function

# an environment is a sequence of frames. local + global + ...