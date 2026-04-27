from utils import readFASTA

with open ('rosalind_edit.txt', 'r') as f:
    content = f.read().splitlines()
sequences = readFASTA(content)
s1, s2 = sequences.values()


n = len(s1)
m = len(s2)

dp = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(n + 1):
    dp[i][0] = i

for j in range(m + 1):
    dp[0][j] = j


for i in range(1, n + 1):
    for j in range(1, m + 1):
        if s1[i - 1] == s2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1]
        else:
            insert = dp[i][j - 1] + 1
            delete = dp[i - 1][j] + 1
            replace = dp[i - 1][j - 1] + 1
            dp[i][j] = min(insert, delete, replace)

print(dp[n][m])