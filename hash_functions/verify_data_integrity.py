import hashlib

data = "transaction data"
original_hash = hashlib.sha256(data.encode()).hexdigest()

#Later
received_data = "transaction data"
newhash = hashlib.sha256(received_data.encode()).hexdigest()

if original_hash == newhash:
    print("Data is intact")
else:
    print("Data has been altered")