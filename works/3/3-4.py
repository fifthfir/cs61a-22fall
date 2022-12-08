x = 2
def f():
    print(x) # not gonna work here if x is(will be) defined
    x = 3 # 
    print(x)
f()

def g(x):
    print(x)
    x = 3
    print(x)
g(x)

x = 2
if x > 1:
    print('go')
if x > 0:
    print('bears')

x = 2
if x > 1:
    print('go')
elif x > 0: #won't work because of the 'el'
    print('bears')

