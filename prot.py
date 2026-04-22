from coding_table import rna_codon_table

with open('rosalind_prot.txt', 'r') as f:
    content = f.read()


protein = ""
for i in range(0, len(content), 3):
    codon = content[i:i+3]
    if codon in rna_codon_table:
        amino_acid = rna_codon_table[codon]
        if amino_acid == 'Stop':
            break
        protein += amino_acid

print(protein)
