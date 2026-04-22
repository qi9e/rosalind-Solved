with open('rosalind_lgis.txt', 'r') as f:
    content = f.read().splitlines()
    n = int(content[0])
    seq = list(map(int, content[1].split()))

crei = seq[:]
s1 = []

while len(crei) > 0:
    min_val = min(crei)
    crei = crei[crei.index(min_val) + 1:]
    s1.append(min_val)

dex = seq[:]
s2 = []

while len(dex) > 0:
    max_val = max(dex)
    dex = dex[dex.index(max_val) + 1:]
    s2.append(max_val)

print(' '.join(map(str, s1)))
print(' '.join(map(str, s2)))


#我发现要求最长的，但是这里使用了贪心算法。
#贪心算法不一定能得到最长的结果。

seq = seq[:]
n = len(seq)

# LIS
tails = []
tail_idx = []
prev_c = [-1] * n

for i in range(n):
    if len(tails) == 0 or seq[i] > tails[-1]:
        prev_c[i] = tail_idx[-1] if tails else -1
        tails.append(seq[i])
        tail_idx.append(i)
    else:
        for j in range(len(tails)):
            if seq[i] <= tails[j]:
                prev_c[i] = tail_idx[j-1] if j > 0 else -1
                tails[j] = seq[i]
                tail_idx[j] = i
                break

idx = tail_idx[-1]
creix = []
while idx != -1:
    creix.append(seq[idx])
    idx = prev_c[idx]
creix.reverse()

# LDS
tails = []
tail_idx = []
prev_d = [-1] * n

for i in range(n):
    if len(tails) == 0 or seq[i] < tails[-1]:
        prev_d[i] = tail_idx[-1] if tails else -1
        tails.append(seq[i])
        tail_idx.append(i)
    else:
        for j in range(len(tails)):
            if seq[i] >= tails[j]:
                prev_d[i] = tail_idx[j-1] if j > 0 else -1
                tails[j] = seq[i]
                tail_idx[j] = i
                break

idx = tail_idx[-1]
decreix = []
while idx != -1:
    decreix.append(seq[idx])
    idx = prev_d[idx]
decreix.reverse()

print ("result for longest  subsequence:")
print(' '.join(map(str, creix)))
print(' '.join(map(str, decreix)))