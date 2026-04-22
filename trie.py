with open('rosalind_trie.txt') as f:
    patterns = [line.strip() for line in f if line.strip()]

trie = {1: {}}
edges = []
next_node = 2

for pattern in patterns:
    current = 1
    for ch in pattern:
        if ch not in trie[current]:
            trie[current][ch] = next_node
            trie[next_node] = {}
            edges.append((current, next_node, ch))
            next_node += 1
        current = trie[current][ch]

for parent, child, ch in edges:
    with open('trieOUT.txt', 'a') as f:
        f.write(f"{parent} {child} {ch}\n")
    