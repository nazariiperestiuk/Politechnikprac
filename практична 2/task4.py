import random

N = 100000
inside_circle = 0

for i in range(N):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x**2 + y**2 <= 1:
        inside_circle += 1

pi_e = 4 * inside_circle / N
print("Оцінка π методом Монте-Карло:", pi_e)

