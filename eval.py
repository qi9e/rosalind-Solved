

with open("rosalind_eval.txt", "r") as f:
    lines = f.read().splitlines()

n = int(lines[0])
s = lines[1]
a = list(map(float, lines[2].split()))

length = len(s)
pos = n - length + 1

respo = []
for i in a:
    prob = 1.0

    for j in s:
        if j == "G" or j == "C":
            prob *= i / 2
        else:
            prob *= (1 - i) / 2
    respo.append(prob * pos)

print(" ".join(map(str, respo)))