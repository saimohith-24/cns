import random
def diffie_hellman(p, g, secret_a, secret_b):
    # Compute public values
    A = pow(g, secret_a, p)
    B = pow(g, secret_b, p)
    # Compute shared secret key
    shared_key_a = pow(B, secret_a, p)
    shared_key_b = pow(A, secret_b, p)
    return A, B, shared_key_a, shared_key_b
# Public parameters
p = 23  # Prime number
g = 5   # Generator
# Alice and Bob choose secret numbers
secret_a = random.randint(1, p-1)
secret_b = random.randint(1, p-1)
# Perform Diffie-Hellman key exchange
A, B, shared_key_a, shared_key_b = diffie_hellman(p, g, secret_a, secret_b)
print(f"Public Parameters: p={p}, g={g}")
print(f"Alice's Secret: {secret_a}")
print(f"Bob's Secret: {secret_b}")
print(f"Alice Sends: {A}")
print(f"Bob Sends: {B}")
print(f"Alice Computes Shared Key: {shared_key_a}")
print(f"Bob Computes Shared Key: {shared_key_b}")
assert shared_key_a == shared_key_b, "Shared keys do not match!"
