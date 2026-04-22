with open('rosalind_iev.txt', 'r') as f:
    content = f.read()
    a, b, c, d, e, f = map(int, content.split())
 
print(2 * (a + b + c) + 1.5 * d + e + 0 * f)