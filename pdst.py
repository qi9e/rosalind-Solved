from utils import readFASTA
with open('rosalind_pdst.txt', 'r') as f:
    content = f.read().splitlines()
    sequences = readFASTA(content)
seq_list = list(sequences.values())

res = [[0] * len(seq_list) for _ in range(len(seq_list))]

for i in range(len(seq_list)):
    for j in range(i + 1, len(seq_list)):
        if i != j:
            count = sum(1 for a, b in zip(seq_list[i], seq_list[j]) if a != b)
            res[i][j] = count / len(seq_list[i])
            res[j][i] = res[i][j]

print('\n'.join(' '.join(f'{x:.5f}' for x in row) for row in res))