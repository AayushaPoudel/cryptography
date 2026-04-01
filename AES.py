# Function to pad message to 16 characters
def pad(text):
    while len(text) % 16 != 0:
        text += ' '
    return text

# XOR function
def xor(a, b):
    return ''.join(chr(ord(x) ^ ord(y)) for x, y in zip(a, b))

# Simple block encryption (AES-like)
def encrypt_block(block, key):
    return xor(block, key)

# Simple block decryption
def decrypt_block(block, key):
    return xor(block, key)

# CBC Encryption
def encrypt(message, key):
    message = pad(message)
    iv = "INITIALVECTOR123"   # 16 char IV (fixed for demo)

    ciphertext = ""
    prev = iv

    for i in range(0, len(message), 16):
        block = message[i:i+16]
        block = xor(block, prev)
        encrypted = encrypt_block(block, key)
        ciphertext += encrypted
        prev = encrypted

    return ciphertext

# CBC Decryption
def decrypt(ciphertext, key):
    iv = "INITIALVECTOR123"
    plaintext = ""
    prev = iv

    for i in range(0, len(ciphertext), 16):
        block = ciphertext[i:i+16]
        decrypted = decrypt_block(block, key)
        plaintext_block = xor(decrypted, prev)
        plaintext += plaintext_block
        prev = block

    return plaintext.strip()

# Main
message = "AAYU_AES_LAB2026"
key = "MYSECRETKEY12345"

cipher = encrypt(message, key)
decrypted = decrypt(cipher, key)

print("Original Message:", message)
print("Encrypted Message:", cipher)
print("Decrypted Message:", decrypted)