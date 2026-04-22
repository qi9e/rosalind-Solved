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

# dp[i][j] = 子串s[i..j]的非交叉完美匹配数
dp = [[0] * n for _ in range(n)]

# 按区间长度从小到大填表
for length in range(2, n + 1, 2):  # 只考虑偶数长度
    for i in range(n - length + 1):
        j = i + length - 1
        # s[i] 和 s[k] 配对，k必须使两侧长度都为偶数
        # 即 k-i 必须为奇数（左侧 i+1..k-1 长度为偶数）
        for k in range(i + 1, j + 1, 2):  # k-i 为奇数
            if can_pair(s[i], s[k]):
                left = dp[i+1][k-1] if k > i + 1 else 1
                right = dp[k+1][j] if k < j else 1
                dp[i][j] = (dp[i][j] + left * right) % MOD

print(dp[0][n-1])