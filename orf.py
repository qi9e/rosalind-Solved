from utils import readFASTA, dna_codon_table

with open('rosalind_orf.txt', 'r') as f:
    content = f.read().splitlines()
    sequences = readFASTA(content)

def rev(seq):
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join(complement[base] for base in reversed(seq))

def find_orfs(seq):
    proteins = set()
    for i in range(len(seq) - 2):
        if seq[i:i+3] == 'ATG':  # 从起始密码子 ATG 开始
            protein = ''
            for j in range(i, len(seq) - 2, 3):
                codon = seq[j:j+3]
                if len(codon) != 3:
                    break
                aa = dna_codon_table.get(codon)
                if not aa:
                    break
                if aa == 'Stop':
                    if protein:
                        proteins.add(protein)
                    break
                protein += aa
    return proteins

results = set()
seq = list(sequences.values())[0]

# 正向链的三个阅读框
for frame in range(3):
    results |= find_orfs(seq[frame:])

# 反向互补链的三个阅读框
rev_seq = rev(seq)
for frame in range(3):
    results |= find_orfs(rev_seq[frame:])

for protein in sorted(results):
    print(protein)