def generate_matrix(key):
    key = key.upper().replace("J", "I")
    matrix = []
    used = set()

    for char in key:
        if char not in used:
            used.add(char)
            matrix.append(char)

    for char in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if char not in used:
            used.add(char)
            matrix.append(char)

    return [matrix[i*5:(i+1)*5] for i in range(5)]

def prepare_text(text):
    text = text.upper().replace("J", "I")
    i = 0
    pairs = []
    while i < len(text):
        a = text[i]
        b = 'X'
        if i+1 < len(text):
            b = text[i+1]
            if a == b:
                b = 'X'
                i += 1
            else:
                i += 2
        else:
            i += 1
        pairs.append((a, b))
    return pairs

def find_position(matrix, char):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == char:
                return i, j

def encrypt_playfair(matrix, pairs):
    result = ""
    for a, b in pairs:
        r1, c1 = find_position(matrix, a)
        r2, c2 = find_position(matrix, b)

        if r1 == r2:
            result += matrix[r1][(c1+1)%5]
            result += matrix[r2][(c2+1)%5]
        elif c1 == c2:
            result += matrix[(r1+1)%5][c1]
            result += matrix[(r2+1)%5][c2]
        else:
            result += matrix[r1][c2]
            result += matrix[r2][c1]
    return result

def decrypt_playfair(matrix, text):
    pairs = [(text[i], text[i+1]) for i in range(0, len(text), 2)]
    result = ""
    for a, b in pairs:
        r1, c1 = find_position(matrix, a)
        r2, c2 = find_position(matrix, b)

        if r1 == r2:
            result += matrix[r1][(c1-1)%5]
            result += matrix[r2][(c2-1)%5]
        elif c1 == c2:
            result += matrix[(r1-1)%5][c1]
            result += matrix[(r2-1)%5][c2]
        else:
            result += matrix[r1][c2]
            result += matrix[r2][c1]
    return result

message = "SECUREMESSAGE"
key = "MONARCHY"

matrix = generate_matrix(key)
pairs = prepare_text(message)

cipher = encrypt_playfair(matrix, pairs)
print("Encrypted:", cipher)

decrypted = decrypt_playfair(matrix, cipher)
print("Decrypted:", decrypted)
