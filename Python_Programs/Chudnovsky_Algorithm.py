import cupy as cp

def chudnovsky_algorithm(n):
    C = 426880 * cp.sqrt(10005)
    K = 6
    M = 1
    X = 1
    L = 13591409
    S = L

    for i in range(1, n):
        M = (K**3 - 16*K) * M // i**3
        L += 545140134
        X *= -262537412640768000
        S += M * L // X
        K += 12

    pi = C / S
    return pi

# Number of terms to calculate
n_terms = 100
pi_value = chudnovsky_algorithm(n_terms)
print(f"Calculated value of π in {n_terms} terms:\n{pi_value}")