

with open('rosalind_rstr.txt') as f:
    data = f.read().strip().split()

N = int(data[0])
x = float(data[1])
s = data[2]

gc = sum(1 for c in s if c in "GC")
at = len(s) - gc

p = (x / 2) ** gc * ((1 - x) / 2) ** at

result = 1 - (1 - p) ** N

print(result)