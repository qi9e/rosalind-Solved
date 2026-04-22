import itertools

with open('rosalind_sign.txt', 'r') as f:
    n = int(f.read().strip())

perms = list(itertools.permutations(range(1, n + 1)))
signs = list(itertools.product([1, -1], repeat=n))

total = len(perms) * len(signs)
print(total)

for perm in perms:
    for sign in signs:
        print(' '.join(str(p * s) for p, s in zip(perm, sign)))