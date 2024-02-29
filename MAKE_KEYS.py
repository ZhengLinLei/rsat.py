#!py

# Sender
from random import choice
import sys

# Change the values
p = int(sys.argv[1])
q = int(sys.argv[2])
m = int(sys.argv[3]) if len(sys.argv) > 3 else 0


# --------------------
def prime(x, y):
    prime_list = []
    for i in range(x, y):
        if i == 0 or i == 1:
            continue
        else:
            for j in range(2, int(i/2)+1):
                if i % j == 0:
                    break
            else:
                prime_list.append(i)
    return prime_list



n = p*q

t = (p-1)*(q-1)
e = choice(prime(2, t))
d = pow(e, -1, t)


c = pow(m, e) % n

print(f'Public key = {e}, N = {n}')
print(f'Cypher {c}')


print("--------")
print(f'Private key = {d}, T = {t}')