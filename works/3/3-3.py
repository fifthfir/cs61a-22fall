def prime1(x):
    a = []
    for i in range(2,x//2+1):
        if x % i == 0 and x > 1:
             a.append(i)
             x //= i
        if x == 1:
            break
        else:
            i += 1
    return a

def prime2(n):
    while n > 1:
        k = smallest_prime_factor(n)
        n //= k
        print(k)
def smallest_prime_factor(n):
    k = 2
    while n % k != 0:
        k += 1
    return k
    # once return, you will get out of the whole function

def prime3(n):
    while n > 1:
        k = 2
        while n % k != 0:
            k += 1
        n = n // k
        print(k)

