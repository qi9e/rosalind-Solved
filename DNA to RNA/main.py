

with open('rosalind_rna.txt', 'r') as f:
    content = f.read()
    rna = content.replace('T', 'U')

print(rna)