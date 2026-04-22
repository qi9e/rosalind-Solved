from utils import readFASTA

with open('rosalind_lcsm.txt', 'r') as f:
    content = f.read().splitlines()
    sequences = readFASTA(content).values()

shortest = min(sequences, key=len)

for length in range(len(shortest), 0, -1):
    for start in range(len(shortest) - length + 1):
        candidate = shortest[start:start+length]
        if all(candidate in seq for seq in sequences):
            print(candidate)
            exit()
        