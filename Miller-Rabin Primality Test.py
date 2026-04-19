import random

def power(a, d, n):
    result = 1
    a = a % n
    while d > 0:
        if d % 2 == 1:
            result = (result * a) % n
        d = d // 2
        a = (a * a) % n
    return result

def miller_rabin(n, k=5):
    if n <= 1 or n == 4:
        return False
    if n <= 3:
        return True

    d = n - 1
    while d % 2 == 0:
        d //= 2

    for _ in range(k):
        a = random.randint(2, n - 2)
        x = power(a, d, n)

        if x == 1 or x == n - 1:
            continue

        while d != n - 1:
            x = (x * x) % n
            d *= 2
            if x == 1:
                return False
            if x == n - 1:
                break
        else:
            return False

    return True


num = 17
if miller_rabin(num):
    print(num, "is probably prime")
else:
    print(num, "is composite")