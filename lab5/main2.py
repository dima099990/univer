s=str(input('Введите строку'))
flag=1
string=''
s=s.lower()
for i in range (len(s)):
    if s[i]!=' ':
        string+=s[i]
print(string)
for i in range(len(s)//2):
    if string[i]!=string[-i-1]:
        flag=0
        break
if flag: print('Палиндром')
else: print('Не палиндром')