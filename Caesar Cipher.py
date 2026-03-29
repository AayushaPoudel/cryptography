def encrypt(text, key):
    result = ""
    for char in text:
        if char.isalpha():
            result += chr((ord(char) - 65 + key) % 26 + 65)
    return result

def decrypt(text, key):
    result = ""
    for char in text:
        if char.isalpha():
            result += chr((ord(char) - 65 - key) % 26 + 65)
    return result

message = "HELLOAAYU"
key = 5

encrypted = encrypt(message, key)
decrypted = decrypt(encrypted, key)

print("Encrypted:", encrypted)
print("Decrypted:", decrypted)
