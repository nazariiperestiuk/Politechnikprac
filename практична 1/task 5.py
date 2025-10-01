import math
s0 = int(input("введіть початокову відстань в метрах: "))
u0 = int(input("введіть початокову швидкість в метрах/с: "))
t = int(input("введіть час в секундах: "))
g = 9.8
s = s0 + u0*t + (g*(t**2))/2
print(round(s, 2))
#----------------------------------------------
a = int(input("введіть велику піввісь орбіти: "))
m1 = int(input("введіть початокову масу в кг: "))
m2 = int(input("введіть кінцеву масу в кг: "))\

p = int(input("введіть період обертання: "))

G = (4 * math.pi**2) * (a**3 /p**2 * (m1 + m2))
print(round(G, 2))


p0 = int(input("початкова сума: "))
persent = int(input("введіть відсоток: "))
time = int(input("введіть час в роках: "))

summ = p0 * ((1 +persent / 100)**time)
print(round(summ, 2))

ab = int(input("введіть ab: "))
bb = int(input("введіть bb: "))
y = int(input("введіть кут в градусах: "))

c = math.sqrt(ab**2 + bb**2 - 2*ab*bb * math.cos(math.radians(y)))
print(math.cos(math.radians(y)))
print(round(c, 2))