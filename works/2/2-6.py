from urllib.request import urlopen
shakespeare = urlopen('http://composingprograms.com/shakespeare.txt')
words = set(shakespeare.read().decode().split())
a = []
for w in words:
    if len(w) == 6 and w[::-1] in words:
        a.append(w)
print(a)
# Pure functions. Functions have some input (their arguments) and return some output (the result of applying them). abs()
# Non-pure functions. In addition to returning a value, applying a non-pure function can generate side effects, which make some change to the state of the interpreter or computer.print()

print(print(1), print(2))
