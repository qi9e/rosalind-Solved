from utils import readFASTA

def can_pair(a, b):
    return (a == 'A' and b == 'U') or (a == 'U' and b == 'A') or \
           (a == 'C' and b == 'G') or (a == 'G' and b == 'C')

with open('rosalind_cat.txt', 'r') as f:
    content = f.read().splitlines()
    sequences = readFASTA(content)

s = ''.join(sequences.values())
n = len(s)
MOD = 1_000_000

dp = [[0] * n for _ in range(n)]


for length in range(2, n + 1, 2):  # 只考虑偶数长度
    for i in range(n - length + 1):
        j = i + length - 1

        for k in range(i + 1, j + 1, 2):  # k-i 为奇数
            if can_pair(s[i], s[k]):
                left = dp[i+1][k-1] if k > i + 1 else 1
                right = dp[k+1][j] if k < j else 1
                dp[i][j] = (dp[i][j] + left * right) % MOD

print(dp[0][n-1])
