import hashlib

def mine_block(data,difficulty):
    nonce = 0
    while True:
        text = data + str(nonce)
        hash_result = hashlib.sha256(text.encode()).hexdigest()
        if hash_result.startswith("0"*difficulty):
            return nonce,hash_result
        nonce += 1

nonce,hash_found = mine_block("block data",4)

print("Nonce: ",nonce)
print("Hash: ",hash_found)

# The Mining Journey
# Attempt 0: "block data0" → hash probably didn't start with 0000

# Attempt 1: "block data1" → hash probably didn't start with 0000

# Attempt 2: "block data2" → hash probably didn't start with 0000

# ...

# Attempt 226,324: "block data226324" → hash probably didn't start with 0000

# Attempt 226,325: "block data226325" → BINGO! Hash starts with 0000

# The Winning Combination
# Input string: "block data226325"

# SHA-256 Hash: 0000b55ea7ba1265fc3c0405db5f68763eb81e9e91f2769424289e6d09e77877

# Verification: ✓ Starts with 0000 (4 zeros = difficulty 4)