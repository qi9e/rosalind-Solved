from math import factorial
from utils import readFASTA

with open('rosalind_pmch.txt', 'r') as f:
    content = f.read().splitlines()
sequences = list (readFASTA(content).values())
sequences = sequences[0]

a = sequences.count('A')
c = sequences.count('C')

print(factorial(a) * factorial(c))
    