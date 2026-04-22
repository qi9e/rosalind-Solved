from utils import readFASTA
with open('rosalind_tran.txt', 'r') as f:
    content = f.read().splitlines()
    sequences = readFASTA(content)
    sequences = list(sequences.values())
s = sequences[0]
t = sequences[1]
ts = 0
tv = 0

transitions = {('A','G'),('G','A'),('C','T'),('T','C')}

for i, j in zip(s, t):
    if i != j:
        if (i, j) in transitions:
            ts += 1
        else:
            tv += 1
print(ts/tv)