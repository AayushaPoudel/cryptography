def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mod_inverse(e, phi):
    for d in range(1, phi):
        if (d * e) % phi == 1:
            return d

def rsa():
    p = 3
    q = 11
    n = p * q
    phi = (p - 1) * (q - 1)

    e = 3
    d = mod_inverse(e, phi)

    msg = 7
    print("Original Message:", msg)

    c = pow(msg, e, n)
    print("Encrypted Message:", c)

    m = pow(c, d, n)
    print("Decrypted Message:", m)

rsa()