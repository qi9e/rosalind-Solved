from utils import aa_mass

with open('rosalind_spec.txt', 'r') as f:
    content = f.read().strip().split()

content = [float(x) for x in content]

result = []

for i in range(1, len(content)):
    mass = content[i] - content[i-1]

    best_aa = None
    best_diff = float('inf')

    for aa, m in aa_mass.items():
        diff = abs(mass - m)
        if diff < best_diff:
            best_diff = diff
            best_aa = aa

    result.append(best_aa)

print(''.join(result))