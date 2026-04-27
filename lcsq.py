from utils import readFASTA

with open('rosalind_lcsq.txt', 'r') as f:
    content = f.read().splitlines()
    sequences = list(readFASTA(content).values())
    s = sequences[0]
    t = sequences[1]

#i will make all the following code as a function to reuse it in the next problem

def longest_common_subsequence(s, t):

    n = len(s)
    m = len(t)

    # dp[i][j] = LCS length of s[:i] and t[:j]
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # fill DP table
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s[i - 1] == t[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # backtrack to build one LCS
    i = n
    j = m
    result = []

    while i > 0 and j > 0:
        if s[i - 1] == t[j - 1]:
            result.append(s[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] >= dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return ''.join(reversed(result))



print(longest_common_subsequence(s, t))