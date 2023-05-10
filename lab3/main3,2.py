import math
from tkinter import *

root = Tk()
root.title('Ви12 Орлов')
text1 = Label(text='Введите число')
text1.grid(column=0, row=0)

A = Entry(width=20)
A.grid(column=1, row=0)

answer = Label(bg='black', fg='white', width=20)
answer.grid(column=0, row=4, columnspan=3)

canvas = Canvas(root, width=250, height=200)
canvas.grid()
img = PhotoImage(file='1.png')
LblImg = Label()
LblImg.image = img
LblImg['image'] = LblImg.image
LblImg.grid(row=5, columnspan=3)

calc = Button(text='Вычислить')
calc.grid(column=2, row=0)


def num1(event):
    x = int(A.get())
    a = 10.2
    if x <= 0:
        answer['text'] = str(math.sqrt(abs(x)) + a ** 2)
    elif 0 < x <= 5:
        answer['text'] = str(x ** 2 - a)
    elif x > 5:
        answer['text'] = str((math.cos(x)) ** 2 + a)


calc.bind('<Button-1>', num1)
root.mainloop()
