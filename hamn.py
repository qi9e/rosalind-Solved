with open("rosalind_hamm.txt", "r") as f:
    content = f.read()
    s, t = content.split()

hamming_distance = 0
for i, j in zip(s, t):
    if i != j:
        hamming_distance += 1

print(hamming_distance)
