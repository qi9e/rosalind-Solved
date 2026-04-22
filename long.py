from utils import readFASTA

with open('rosalind_long.txt', 'r') as f:
    content = f.read().splitlines()
    sequences = readFASTA(content)

sequences = list(sequences.values())

def overlap(a, b):
    min_overlap = len(a) // 2 + 1
    max_overlap = min(len(a), len(b))
    for i in range(max_overlap, min_overlap - 1, -1):
        if a[-i:] == b[:i]:
            return i
    return 0

next_read = {}
prev_read = {}
ov = {}

for i in sequences:
    for j in sequences:
        if i != j:
            k = overlap(i, j)
            if k > 0:
                next_read[i] = j
                prev_read[j] = i
                ov[(i, j)] = k

start = None
for seq in sequences:
    if seq not in prev_read:
        start = seq
        break

result = start
cur = start

while cur in next_read:
    nxt = next_read[cur]
    result += nxt[ov[(cur, nxt)]:]
    cur = nxt

print(result)