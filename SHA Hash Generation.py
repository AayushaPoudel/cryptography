import hashlib

def generate_sha(message):
    result = hashlib.sha256(message.encode())
    return result.hexdigest()

# Example
msg = "HelloWorld"
hash_value = generate_sha(msg)

print("Message:", msg)
print("SHA-256 Hash:", hash_value)