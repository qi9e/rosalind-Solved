#aquest ejercici podem resoldre facilment amb un set, ja que el que volem es saber quines lletres apareixen a la segona cadena pero no a la primera

with open("rosalind_seto.txt", "r") as f:
    lines = f.read().splitlines()

n = int(lines[0])

#creem un set amb les lletres de la primera cadena
A = set(map(int, lines[1].strip("{}").replace(" ", "").split(","))) if lines[1] != "{}" else set()
B = set(map(int, lines[2].strip("{}").replace(" ", "").split(","))) if lines[2] != "{}" else set()

U = set(range(1, n + 1)) 

answer =  [
    A | B,      # union
    A & B,      # intersection
    A - B,      # A-B
    B - A,      # B-A
    U - A,      # Ac
    U - B       # Bc
]

for ans in answer:
    with open("setoOUT.txt", "a") as f:
        f.write("{" + ", ".join(map(str, sorted(ans))) + "}\n")

