from utils import readFASTA, kmers

with open('rosalind_kmer.txt', 'r') as f:
    content = f.read().splitlines()
    sequences = readFASTA(content)
s = ''.join(sequences.values())

count = {k: 0 for k in kmers}
for i in range(len(s) - 3):
    kmer = s[i:i+4]
    if kmer in count:
        count[kmer] += 1

print(' '.join(str(count[k]) for k in kmers))
