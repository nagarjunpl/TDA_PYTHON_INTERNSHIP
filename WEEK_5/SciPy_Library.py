import numpy as np
from scipy import stats, optimize

# Normal distribution (statistics)
data = [2, 4, 4, 4, 5, 5, 7, 9]
print("Mean:", np.mean(data))
print("Mode:", stats.mode(data))

# Optimization (find x that minimizes function)
def f(x):
    return x**2 + 5*np.sin(x)

result = optimize.minimize(f, x0=0)  # start at x=0
print("Minimum at:", result.x)
