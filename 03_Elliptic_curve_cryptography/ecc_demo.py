from ecdsa import SigningKey, SECP256k1
 
# Generate private key on secp256k1 curve
private_key = SigningKey.generate(curve=SECP256k1)
 
# Derive public key from private key
public_key = private_key.get_verifying_key()
 
print("Private Key: ", private_key.to_string().hex())
print("Public Key:  ", public_key.to_string().hex())