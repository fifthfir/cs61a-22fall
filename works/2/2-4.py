from re import A


def f(x):
    return g(x+1) + 2
def g(x):
    return x + 3
print(f(7))

a = 1
b = 2
b, a = a + b, b #add before change
res1 = print(2+3,a) #print(res1+7) ERROR
res2 = min(2+3,a)
print(res2+7)