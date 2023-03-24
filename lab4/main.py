import math

q = int(150)
v = int(10000)
c0 = int(10)
t = float(0)
c = float(1)
while c > 0.1:
    c = c0 * math.exp(-q * t / v)
    t = t + 0.5
else:
    c = round(c, 3)
    print("Остаточное содержание хлорки: ", c)
    print("Прошедшее время : ", t, "ч.")
