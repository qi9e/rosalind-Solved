from utils import readFASTA

with open('rosalind_kmp.txt', 'r') as f:
    content = f.read().splitlines()
    sequences = readFASTA(content)
    s = ''.join(sequences.values())

p = [0] * len(s)

for i in range(1, len(s)):
    j = p[i - 1]

    while j > 0 and s[i] != s[j]:
        j = p[j - 1]

    if s[i] == s[j]:
        j += 1

    p[i] = j

with open('kmpOUT.txt', 'w') as f:
    f.write(' '.join(map(str, p)))