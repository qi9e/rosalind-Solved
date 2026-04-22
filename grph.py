from utils import readFASTA

with open('rosalind_grph.txt', 'r') as f:
    content = f.read().splitlines()
    sequences = readFASTA(content)

for id, seq in sequences.items():
    for id2, seq2 in sequences.items():
        if id != id2 and seq[-3:] == seq2[:3]:
            print(id, id2)
