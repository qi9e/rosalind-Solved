with open ('rosalind_inod.txt', 'r') as f:
    content = f.read().splitlines()


print(int(content[0]) - 2)