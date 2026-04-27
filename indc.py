import math

with open("rosalind_indc.txt", "r") as f:
    n = int(f.read().strip())

total = 2 * n
answers = []

for k in range(1, total + 1):
    prob = 0

    for i in range(k, total + 1):
        prob += math.comb(total, i) * (0.5 ** total)

    answers.append(math.log10(prob))

print(" ".join(f"{x:.6f}" for x in answers))