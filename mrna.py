from utils import codon_count

with open('rosalind_mrna.txt', 'r') as f:
    content = f.read().strip()

MOD = 1_000_000
res = 1
for aa in content:
    res = (res * codon_count[aa]) % MOD

res = (res * 3) % MOD 
print(res)