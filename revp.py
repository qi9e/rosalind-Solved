from utils import readFASTA, rev_comp

with open('rosalind_revp.txt', 'r') as f:
    content = f.read().splitlines()
    sequences = list(readFASTA(content).values())

seq = sequences[0]

for i in range(len(seq)):
    for j in range(4, 13):
        if i + j <= len(seq):
            subseq = seq[i:i+j]
            if subseq == rev_comp(subseq):
                print(i+1, j)
