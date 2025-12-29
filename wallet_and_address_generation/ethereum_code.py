from eth_account import Account

acct = Account.create()

print("Private Key: ",acct.key.hex())
print("Address: ",acct.address)


# STEPS
# Generate private key
# Derive public key (ECC secp256k1)
# Hash public key using Keccak-256
# Take last 20 bytes
# Apply EIP-55 checksum

# THIS CODE ALREADY INCLUDES:
# Keccak-256
# Last 20 bytes
# EIP-55 checksum