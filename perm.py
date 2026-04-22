from itertools import permutations
import math

with open('rosalind_perm.txt', 'r') as f:
    content = f.read().strip()


perms = list(permutations(range(1, int(content) + 1)))
print(math.factorial(int(content)))

for p in perms:
    print(' '.join(map(str, p)))
