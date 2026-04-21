import hashlib

def generate_md5(message):
    result = hashlib.md5(message.encode())
    return result.hexdigest()

# Example
msg = "HelloWorld"
hash_value = generate_md5(msg)

print("Message:", msg)
print("MD5 Hash:", hash_value)