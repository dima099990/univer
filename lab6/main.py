import math

print('Расчет формулы: R[i]=tg(D[i])^2-ctg(b*d[i])/2b+1')
d = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = int(input("Введите число b= : "))
r = []
x = float(0)
sum=float(0)

# for i in range(10):
#     d.append(int(input(""'Введите число D['+str(i+1)+']')))


for i in range(len(d)):
    x = (((math.tan(d[i]) ** 2)) - math.tan(b * d[i])) / 2 * b + 1
    r.append(round(x, 3))
    if i % 2 == 0:
        sum=sum+r[i]
# print(r[i])
maximum = max(r)
minimum = min(r)

print(r)
for i in range(len(r)):
  if r[i] == maximum:
    r[i] = minimum
  elif r[i] == minimum:
    r[i] = maximum



# print(d)
print(r)
print('Сумма четных элементов',sum)


