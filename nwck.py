from utils import parse_newick
from collections import deque

with open('rosalind_nwck.txt', 'r') as f:
    newick_str = f.read().strip()

lines = [line.strip() for line in newick_str.splitlines() if line.strip()]

def distance(graph, start, end):
    if start == end:
        return 0
    
    queue = deque([(start, 0)])
    visited = {start}

    while queue:
        node, dist = queue.popleft()
        if node == end:
            return dist

        for nei in graph[node]:
            if nei not in visited:
                visited.add(nei)
                queue.append((nei, dist + 1))
    
    return -1  # No path found

i = 0
results = []

while i < len(lines):
    tree = lines[i]
    if i + 1 >= len(lines):
        break
    
    x, y = lines[i + 1].split()
    i += 2

    graph, name_to_id = parse_newick(tree)

    if x not in name_to_id or y not in name_to_id:
        print(f"Warning: {x} or {y} not in tree")
        continue

    start = name_to_id[x]
    end = name_to_id[y]

    d = distance(graph, start, end)
    results.append(str(d))

print(' '.join(results))