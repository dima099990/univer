import math

print('Расчет формулы: R[i]=tg(D[i])^2-ctg(b*d[i])/2b+1')
d = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = int(input("Введите число b= : "))
r = []
x = float(0)

# for i in range(10):
#     d.append(int(input(""'Введите число D['+str(i+1)+']')))


for i in range(len(d)):
    x = (((math.tan(d[i]) ** 2)) - math.tan(b * d[i])) / 2 * b + 1
    r.append(round(x, 3))
    # print(r[i])

print(d)
print(r)
