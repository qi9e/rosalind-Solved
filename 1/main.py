


a = 0
b =0
c = 0
d = 0

with open('rosalind_dna.txt', 'r') as f:
    content = f.read()
    for i in content:
        if i == 'A':
            a += 1
        elif i == 'C':
            b += 1
        elif i == 'G':
            c += 1
        elif i == 'T':
            d += 1

print(a, b, c, d)