with open('rosalind_tree.txt', 'r') as f:
    content = f.read()

lines = content.strip().split('\n')
n = int(lines[0])
edges = [list(map(int, line.split())) for line in lines[1:]]

parents = {}

def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]

for i in range(1, n + 1):
    parents[i] = i

for u, v in edges:
    u_root = find(u)
    v_root = find(v)
    if u_root != v_root:
        parents[u_root] = v_root

roots = set()

for i in range(1, n + 1):
    roots.add(find(i))

k = len(roots)
print(k - 1)