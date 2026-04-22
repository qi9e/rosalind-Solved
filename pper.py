with open ('rosalind_pper.txt', 'r') as f:
    content = f.read()
    n, m = map(int, content.split())

p = 1 
for i in range (m):
    p *= (n - i)

print(p%1000000)