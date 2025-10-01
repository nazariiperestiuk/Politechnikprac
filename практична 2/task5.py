import math

N = 100000
s = 0

for k in range(N):
    s += ((-1)**k) / (2*k + 1)

pi = 4 * s
error = abs(math.pi - pi)

print(f" число пі для N = {N} :, {pi}")
print(f"Похибка: {error}")
