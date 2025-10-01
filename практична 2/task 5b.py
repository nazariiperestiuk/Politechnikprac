import math

err = 1e-5
s = 0
k = 0

while True:
    s += ((-1)**k) / (2*k + 1)
    pi = 4 * s
    error = abs(math.pi - pi)
    if error < err:
        break
    k += 1

print("число пі:", pi)
print("Кількість членів ряду:", k+1)
print("Фактична похибка:", error)
