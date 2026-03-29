import numpy as np

def mod_inverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None

def hill_encrypt(message, key):
    message = message.upper()
    msg_vector = [ord(i) - 65 for i in message]
    key_matrix = np.array(key)

    result = np.dot(key_matrix, msg_vector) % 26
    return ''.join([chr(i + 65) for i in result])

def hill_decrypt(cipher, key):
    key_matrix = np.array(key)
    det = int(np.round(np.linalg.det(key_matrix)))
    det_inv = mod_inverse(det % 26, 26)

    adj = np.round(det * np.linalg.inv(key_matrix)).astype(int) % 26
    inv_key = (det_inv * adj) % 26

    cipher_vector = [ord(i) - 65 for i in cipher]
    result = np.dot(inv_key, cipher_vector) % 26

    return ''.join([chr(int(i) + 65) for i in result])

message = "HI"
key = [[3, 3], [2, 5]]

encrypted = hill_encrypt(message, key)
decrypted = hill_decrypt(encrypted, key)

print("Encrypted:", encrypted)
print("Decrypted:", decrypted)
