import hashlib

def sha256(data):
    return hashlib.sha256(data.encode()).hexdigest()

print(sha256("hello"))
print(sha256("Hello"))

# Observe completely different hashes.