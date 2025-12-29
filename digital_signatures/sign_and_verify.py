from ecdsa import SigningKey, SECP256k1
import hashlib

private_key = SigningKey.generate(curve=SECP256k1)
public_key = private_key.get_verifying_key()

message = b"Send 2 ETH to Bob"

#Hash message
message_hash = hashlib.sha256(message).digest()

#Sign
signature = private_key.sign(message_hash)

#Verify
is_valid = public_key.verify(signature,message_hash)
print("Signature valid?", is_valid)
 

# How Messages Are Signed
# Message (transaction data)
#         ↓
# Hash the message
#         ↓
# Sign hash using PRIVATE KEY
#         ↓
# Signature created

# How Signatures Are Verified
# Message + Signature + Public Key
#         ↓
# Hash message again
#         ↓
# Verify signature using PUBLIC KEY
#         ↓
# Valid or Invalid
