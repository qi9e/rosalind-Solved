from utils import readFASTA

with open('rosalind_sseq.txt', 'r') as f:
    content = f.read().splitlines()
    sequences = list(readFASTA(content).values())

s = sequences[0]  
t = sequences[1]

positions = []
pos = 0

for char in t:
    try:
        index = s.index(char, pos)
        positions.append(index + 1)  # 1-indexed
        pos = index + 1
    except ValueError:
        break

print(' '.join(map(str, positions)))
