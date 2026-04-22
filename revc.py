


with open("rosalind_revc.txt", "r") as f:
    content = f.read()


reversed = content[::-1]

for i in reversed:
    if i == "A":
        print("T", end="")
    elif i == "C":
        print("G", end="")
    elif i == "G":
        print("C", end="")
    elif i == "T":
        print("A", end="")