#creo que ya he imprementado reverse complement, pero lo dejo aqui por si acas
#porque no he econtrada el ejercicio de reverse complement, pero lo dejo aqui por si acaso

def reverse_complement(s):
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join(complement[i] for i in reversed(s))


with open("rosalind_dbru.txt", "r") as f:
    content = f.read().splitlines()

all = set()

for line in content:
    all.add(line)
    all.add(reverse_complement(line))

edges = set()

for s in all:
    prefix = s[:-1]
    suffix = s[1:]
    edges.add((prefix, suffix))

for prefix, suffix in edges:
    with open("dbruOUT.txt", "a") as f:
        f.write(f"{prefix} {suffix}\n")