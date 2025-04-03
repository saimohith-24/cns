import math
def gcd_extended(a, b):
    """Extended Euclidean Algorithm to find modular inverse"""
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = gcd_extended(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y
# Given public key parameters
e = 31
n = 3599
# Step 1: Find p and q through trial-and-error (factorizing n)
def find_prime_factors(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return i, n // i
    return None, None
p, q = find_prime_factors(n)
if not p or not q:
    raise ValueError("Failed to factorize n")
# Step 2: Compute Euler's Totient function phi(n)
phi_n = (p - 1) * (q - 1)
# Step 3: Compute private key d (modular inverse of e mod phi(n))
_, d, _ = gcd_extended(e, phi_n)
# Ensure d is positive
d = d % phi_n
print(f"Public Key (e, n): ({e}, {n})")
print(f"Prime factors: p = {p}, q = {q}")
print(f"Euler's Totient (φ(n)): {phi_n}")
print(f"Private Key (d, n): ({d}, {n})")
