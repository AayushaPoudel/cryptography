def diffie_hellman():
    p = 23   # prime number
    g = 5    # primitive root

    a = 6    # private key of A
    b = 15   # private key of B

    A = pow(g, a, p)
    B = pow(g, b, p)

    key_A = pow(B, a, p)
    key_B = pow(A, b, p)

    print("Public values: p =", p, "g =", g)
    print("Private keys: a =", a, "b =", b)
    print("Computed keys:")
    print("A computes:", key_A)
    print("B computes:", key_B)

diffie_hellman()