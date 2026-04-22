from utils import readFASTA
from functools import lru_cache

with open('rosalind_motz.txt', 'r') as f:
    content = f.read().splitlines()
    sequences = readFASTA(content)

s = ''.join(sequences.values())

MOD = 1000000

def can_pair(a, b):
    return (a == "A" and b == "U") or \
           (a == "U" and b == "A") or \
           (a == "C" and b == "G") or \
           (a == "G" and b == "C")

@lru_cache(maxsize=None)
def solve(i, j):
    if i >= j:
        return 1

    # 情况1：s[i] 不配对
    total = solve(i + 1, j)

    # 情况2：s[i] 和某个 k 配对
    for k in range(i + 1, j + 1):
        if can_pair(s[i], s[k]):
            total += solve(i + 1, k - 1) * solve(k + 1, j)
            total %= MOD

    return total % MOD

print(solve(0, len(s) - 1))