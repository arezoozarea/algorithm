import numpy as np

n = 3
a = np.array([1, 2, 3, 4, 5, 6, 9, 8, 9])
s = 0
s2 = len(a) - n
sum1 = 0
sum2 = 0
for _ in range(n):
    sum1 += a[s]
    sum2 += a[s2]

    s2 -= n - 1
    s += n + 1
print(abs(sum1 - sum2))

