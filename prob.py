import math

with open('rosalind_prob.txt', 'r') as f:
    content = f.read()
    seq, pro = content.splitlines()
    pro = list(map(float, pro.split()))

result = []
gc_count = seq.count('G') + seq.count('C')
at_count = seq.count('A') + seq.count('T')

for x in pro:
    gc = x/2
    at = (1-x)/2

    log = (math.log10(gc) * gc_count) + (math.log10(at) * at_count)
    result.append(log)

print(*result)