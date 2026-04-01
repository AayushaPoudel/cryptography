# Function to find GCD using Euclidean Algorithm
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Extended Euclidean Algorithm
def extended_euclid(a, m):
    if m == 0:
        return a, 1, 0
    gcd_val, x1, y1 = extended_euclid(m, a % m)
    x = y1
    y = x1 - (a // m) * y1
    return gcd_val, x, y

# Additive Inverse
def additive_inverse(a, m):
    return (m - a) % m

# Multiplicative Inverse
def multiplicative_inverse(a, m):
    gcd_val, x, y = extended_euclid(a, m)
    if gcd_val != 1:
        return None
    else:
        return x % m

# Main Program
a = 17
m = 43

print("Given values:")
print("a =", a, ", m =", m)

# Additive Inverse
add_inv = additive_inverse(a, m)
print("\nAdditive Inverse of", a, "mod", m, "=", add_inv)

# Check relatively prime
g = gcd(a, m)
print("\nGCD(", a, ",", m, ") =", g)

if g == 1:
    print("They are relatively prime")
else:
    print("They are not relatively prime")

# Multiplicative Inverse
mul_inv = multiplicative_inverse(a, m)

if mul_inv is not None:
    print("\nMultiplicative Inverse of", a, "mod", m, "=", mul_inv)
else:
    print("\nMultiplicative inverse does not exist")