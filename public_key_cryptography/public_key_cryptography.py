# 1. Create transaction
# 2. Sign with private key → digital signature
# 3. Send tx + signature
# 4. Network verifies signature using public key
# 5. Tx accepted if valid

from ecdsa import SigningKey,SECP256k1

# Generate a private key
private_key = SigningKey.generate(curve=SECP256k1)
public_key = private_key.get_verifying_key()

message = b"Send 1 BTC to Alice" #Basically message here represents transaction

#Sign the message
signature = private_key.sign(message)
print("Signature: ",signature.hex())

#Verify the signature

is_valid = public_key.verify(signature,message)
print("Signature valid?", is_valid)

