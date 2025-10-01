a = int(input("write a: "))
b = int(input("write b: "))
c = int(input("write c: "))
discriminant = b**2 - 4*a*c
x1 = (-b - discriminant**0.5)/(2*a)
x2 = (-b + discriminant**0.5)/(2*a)
if discriminant < 0 :
    print("рння не має розвязків")
elif discriminant == 0:
    x = -b/(2 * a)
    print(round(x,2))
else :
    print(round(x1, 2), round(x2, 2))