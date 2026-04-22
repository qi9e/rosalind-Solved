
with open('rosalind_fib.txt', 'r') as f:
    content = f.read()
    n, k = map(int, content.split())

a, b = 1, 1
for i in range (3, n+1):
    a, b = b, a * k + b
    print(a, b)

print(b)