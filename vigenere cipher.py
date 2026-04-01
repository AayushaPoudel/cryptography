def generate_key(message, key):
    key = list(key)
    if len(message) == len(key):
        return key
    else:
        for i in range(len(message) - len(key)):
            key.append(key[i % len(key)])
    return "".join(key)

def encrypt(message, key):
    cipher_text = []
    for i in range(len(message)):
        x = (ord(message[i]) + ord(key[i])) % 26
        x += ord('A')
        cipher_text.append(chr(x))
    return "".join(cipher_text)

def decrypt(cipher_text, key):
    orig_text = []
    for i in range(len(cipher_text)):
        x = (ord(cipher_text[i]) - ord(key[i]) + 26) % 26
        x += ord('A')
        orig_text.append(chr(x))
    return "".join(orig_text)

message = "HELLOCRYPTOGRAPHY"
key = "KEY"

new_key = generate_key(message, key)

cipher_text = encrypt(message, new_key)
print("Encrypted:", cipher_text)

decrypted_text = decrypt(cipher_text, new_key)
print("Decrypted:", decrypted_text)







