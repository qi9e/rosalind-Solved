from utils import readFASTA

with open('rosalind_cons.txt', 'r') as f:
    content = f.read().splitlines()
    sequences = readFASTA(content)
    
coutA = []
coutC = []
coutG = []
coutT = []

dna = sequences.values()
columns = list(zip(*dna))

for column in columns:
    coutA.append(column.count('A'))
    coutC.append(column.count('C'))
    coutG.append(column.count('G'))
    coutT.append(column.count('T'))

for i in range(len(columns)):
    if coutA[i] >= coutC[i] and coutA[i] >= coutG[i] and coutA[i] >= coutT[i]:
        print('A', end="")
    elif coutC[i] >= coutA[i] and coutC[i] >= coutG[i] and coutC[i] >= coutT[i]:
        print('C', end="")
    elif coutG[i] >= coutA[i] and coutG[i] >= coutC[i] and coutG[i] >= coutT[i]:
        print('G', end="")
    elif coutT[i] >= coutA[i] and coutT[i] >= coutC[i] and coutT[i] >= coutG[i]:
        print('T', end="")

print('A: ' + ' '.join(map(str, coutA)))
print('C: ' + ' '.join(map(str, coutC)))
print('G: ' + ' '.join(map(str, coutG)))
print('T: ' + ' '.join(map(str, coutT)))