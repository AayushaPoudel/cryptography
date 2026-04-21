def mod_inverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i

def elgamal():
    p = 23
    g = 5
    x = 6   # private key

    y = pow(g, x, p)

    msg = 10
    k = 3

    c1 = pow(g, k, p)
    c2 = (msg * pow(y, k, p)) % p

    print("Original Message:", msg)
    print("Encrypted:", (c1, c2))

    s = pow(c1, x, p)
    s_inv = mod_inverse(s, p)

    m = (c2 * s_inv) % p
    print("Decrypted Message:", m)

elgamal()