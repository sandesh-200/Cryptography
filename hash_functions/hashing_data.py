import hashlib

data = "hello blockchain"

hash_object = hashlib.sha256(data.encode())
hash_hex = hash_object.hexdigest()

print(data.encode())
print(hash_object)
print(hash_hex)