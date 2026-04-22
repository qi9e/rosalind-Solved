from utils import aa_mass

with open('rosalind_prtm.txt', 'r') as f:
    content = f.read().strip()

aa_mass_sum = sum(aa_mass[aa] for aa in content)
print(aa_mass_sum)