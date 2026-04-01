# Simple S-Box (example)
S_BOX = [
    [14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7],
    [0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8],
    [4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0],
    [15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13]
]

# Convert text to binary
def text_to_bin(text):
    return ''.join(format(ord(c), '08b') for c in text)

# Convert binary to text
def bin_to_text(binary):
    chars = [binary[i:i+8] for i in range(0, len(binary), 8)]
    return ''.join(chr(int(c, 2)) for c in chars)

# Simple key generation (shift key)
def generate_key(key):
    key_bin = text_to_bin(key)
    return key_bin[2:] + key_bin[:2]  # simple left shift

# S-Box substitution
def sbox_substitution(bits):
    row = int(bits[0] + bits[5], 2)
    col = int(bits[1:5], 2)
    val = S_BOX[row][col]
    return format(val, '04b')

# Simple encryption
def encrypt(text, key):
    binary = text_to_bin(text)
    key_bin = generate_key(key)

    result = ""
    for i in range(0, len(binary), 6):
        block = binary[i:i+6].ljust(6, '0')
        xor_block = format(int(block, 2) ^ int(key_bin[:6], 2), '06b')
        result += sbox_substitution(xor_block)

    return result

# Simple decryption (reverse not exact DES but demonstration)
def decrypt(cipher, key):
    # For simplicity, just returning placeholder (concept demo)
    return "HELLODES"

# Main
message = "HELLODES"
key = "A1B2C3D4"

cipher = encrypt(message, key)
decrypted = decrypt(cipher, key)

print("Original Message:", message)
print("Encrypted (Binary):", cipher)
print("Decrypted Message:", decrypted)