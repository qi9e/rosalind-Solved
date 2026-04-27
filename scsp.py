from lcsq import longest_common_subsequence

with open('rosalind_scsp.txt') as f:
    content = f.read().strip().splitlines()

s1 = content[0]
s2 = content[1]

lcs = longest_common_subsequence(s1, s2)

i = 0
j = 0
ans = []

for c in lcs:
    while s1[i] != c:
        ans.append(s1[i])
        i += 1

    while s2[j] != c:
        ans.append(s2[j])
        j += 1

    ans.append(c)
    i += 1
    j += 1

# lo que quedan
ans.extend(s1[i:])
ans.extend(s2[j:])

print("here star the answer of scsp \n")

print(''.join(ans))

#cuidado porque imprimen resultado de lcsq. no hay que tener en cuenta