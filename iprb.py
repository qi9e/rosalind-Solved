with open('rosalind_iprb.txt') as f:
    k, m, n = map(int, f.read().split())

T = k + m + n

p_recessive = (
    n * (n - 1) / (T * (T - 1)) +
    m * n / (T * (T - 1)) +
    m * (m - 1) / (4 * T * (T - 1))
)

p_dominant = 1 - p_recessive

print(p_dominant)