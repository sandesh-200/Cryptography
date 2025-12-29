from ecdsa import SigningKey,SECP256k1

private_key = SigningKey.generate(curve=SECP256k1)

public_key = private_key.get_verifying_key()

print("Private Key: ",private_key.to_string().hex())
print("Public Key: ",public_key.to_string().hex())