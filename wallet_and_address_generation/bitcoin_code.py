import hashlib

def hash(pub_key):
    sha = hashlib.sha256(pub_key).digest()
    ripemd = hashlib.new('ripemd160',sha).digest()
    return ripemd

# BITCOIN STEPS
# Generate private key
# Derive public key (ECC)
# SHA-256(public key)
# RIPEMD-160(result)
# Add network prefix
# Base58 encode