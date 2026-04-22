with open('rosalind_fibd.txt', 'r') as f:
    content = f.read()
    n, m = map(int, content.split())

# ages[k] = number of rabbit pairs that are k months old (0-indexed: age 0 = newborn)
ages = [0] * m
ages[0] = 1  # month 1: one newborn pair

for i in range(2, n + 1):
    # newborns = sum of all mature pairs (age >= 1)
    newborns = sum(ages[1:])
    # age everyone by one month, oldest die (fall off the end)
    ages = [newborns] + ages[:-1]

print(sum(ages))