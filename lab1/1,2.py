import math

print('расчет формулы d=((f+g)^1-h)+(2/(9*g*h-(math.fabs(g-f-h^2)))) ')

f = 6
g = 4
h = 12
print("F= ",f)
print("g= ",g)
print("H= ",h)
d = ((f + g) ^ 1 - h) + (2 / (9 * g * h - (math.fabs(g - f - h ^ 2))))
print(d)
