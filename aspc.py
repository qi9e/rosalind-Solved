with open ('rosalind_aspc.txt', 'r') as f:
    content = f.read().strip()

n, m = map(int, content.split())


def count_combinations_at_least(n, m, mod=1_000_000):
    row = [0] * (n + 1)
    row[0] = 1
    for i in range(1, n + 1):
        for j in range(i, 0, -1):
            row[j] = (row[j] + row[j - 1]) % mod
    return sum(row[m:]) % mod


print(count_combinations_at_least(n, m))