# public prime and primitive root
p = 23
g = 5

# private keys for Alice and Bob
alice_private_key = 6
bob_private_key = 15

# public keys for Alice and Bob
alice_public_key = (g**alice_private_key) % p
bob_public_key = (g**bob_private_key) % p

# shared secret key calculated by Alice
alice_shared_secret = (bob_public_key**alice_private_key) % p

# shared secret key calculated by Bob
bob_shared_secret = (alice_public_key**bob_private_key) % p

# shared secret key should be the same for both Alice and Bob
assert alice_shared_secret == bob_shared_secret
