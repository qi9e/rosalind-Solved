from itertools import product

with open('rosalind_lexf.txt', 'r') as f:
    content = f.read().splitlines()

aa = content[0]
n = int(content[1])

for combo in product(aa, repeat=n):
    result = ''.join(combo).replace(' ', '')
    if len(result) == 3:
        print(result)

