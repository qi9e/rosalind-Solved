from utils import rna_codon_table, readFASTA

with open('rosalind_splc.txt', 'r') as f:
    content = f.read().splitlines()
    sequences = list(readFASTA(content).values())

exons = sequences[0]
introns = sequences[1:]

for seq in introns:
    exons = exons.replace(seq, '')
mrna = exons.replace('T', 'U')

protein = ''
for i in range(0, len(mrna) - 2, 3):
    codon = mrna[i:i+3]
    aa = rna_codon_table.get(codon)
    if aa == 'Stop':
        break
    if aa:
        protein += aa

print(protein)