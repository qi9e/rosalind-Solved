
with open('rosalind_subs.txt', 'r') as f:
    content = f.read()
    s, t = content.split()

positions = []
for i in range(1+ len(s) - len(t)):
    if s[i:i+len(t)] == t:
        positions.append(i + 1)

print (str(positions).replace('[', '').replace(']', '').replace(',', ''))