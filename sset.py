import math

with open ('rosalind_sset.txt', 'r') as f:
    content = f.read().splitlines()

n = int(content[0])

print(2**n % 1000000)