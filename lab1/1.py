import random

N = int(input('Введите кол-во секунд: '))
while N >= 3601:
    N = N - 3600
print("Число секунд с начала прошлого часа: ", N)
m = int(N / 60)
print("Целые минуты с начала последнего часа:", m)
##test kak eto rabotaet)))