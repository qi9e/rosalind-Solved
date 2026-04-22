from utils import readFASTA

with open('rosalind_cat.txt', 'r') as f:
    content = f.read().splitlines()
    sequences = readFASTA(content)

result = ''.join(sequences.values())

# calcu de correct y incorrect pairs

pair = [('A', 'U'), ('U', 'A'), ('C', 'G'), ('G', 'C')]

correct = []
tmp = []

for dna in result:
    if dna in tmp:
        correct.append((tmp[-1], dna))
    tmp.append(dna)

## hemos contado pares repetrido, ahora vemos repetidos de inversos

def invert(dna):
    tmp = []
    for i in dna:
        if i == 'A':
            tmp.append('U')
        elif i == 'U':
            tmp.append('A')
        elif i == 'C':
            tmp.append('G')
        elif i == 'G':
            tmp.append('C')
    return ''.join(tmp)

inverted = []
for dna in tmp:
    inverted.append(invert(dna))
tmp = []
for dna in inverted:
    if dna in tmp:
        correct.append((tmp[-1], invert(dna)))
    tmp.append(dna)

print(correct)