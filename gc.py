def gc_counter (seq):
    count = seq.count('G') + seq.count('C')
    return count / len(seq) * 100

with open('rosalind_gc.txt', 'r') as f:
    content = f.read().splitlines()

sequences = {}
id = ''

for line in content:
    if line.startswith('>'):
        id = line[1:]
        sequences[id] = ''
    else:
        sequences[id] += line.strip()

max_id = ''
max_gc = 0

for id, seq in sequences.items():
    gc = gc_counter(seq)
    if gc > max_gc:
        max_gc = gc
        max_id = id

print(max_id)
print(max_gc)
