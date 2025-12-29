from eth_account import Account
from eth_account.messages import encode_defunct

Account.enable_unaudited_hdwallet_features()

private_key = Account.create().key
message = "Send 1 ETH"

msg = encode_defunct(text=message)

signed = Account.sign_message(msg,private_key)
print("Signed: ",signed)

print("r: ",signed.r)
print("s: ",signed.s)
print("v: ",signed.v)

#Recover adderss
recovered = Account.recover_message(msg,signature=signed.signature)

print("Recovered address:", recovered)


# Ethereum Signature Flow:
# message → hash → sign with PRIVATE KEY → (r, s, v)
# verify: hash(message) + (r, s, v) → recover PUBLIC KEY
# public key → keccak256 → address
# if recovered address matches sender → signature is valid
