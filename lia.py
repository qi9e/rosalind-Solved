from math import comb

with open("rosalind_lia.txt", "r") as f:
    k, N = map(int, f.read().split())

total = 2 ** k
p = 0

for i in range(N, total + 1):
    p += comb(total, i) * (0.25 ** i) * (0.75 ** (total - i))

print(p)