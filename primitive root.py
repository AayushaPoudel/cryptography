def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def phi(n):
    result = n
    p = 2
    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n //= p
            result -= result // p
        p += 1
    if n > 1:
        result -= result // n
    return result

def is_primitive_root(g, n):
    required_set = set()
    for i in range(1, n):
        required_set.add(pow(g, i, n))
    return len(required_set) == phi(n)

def primitive_roots(n):
    roots = []
    for g in range(2, n):
        if gcd(g, n) == 1 and is_primitive_root(g, n):
            roots.append(g)
    return roots


n = 7
print("Primitive roots of", n, "are:", primitive_roots(n))