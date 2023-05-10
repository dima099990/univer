import math
from tkinter import *

root = Tk()
root.title('ВИ12 Орлов')
root.geometry('400x400')
array = []
inp1 = Label(text='Введите k1')
inp2 = Label(text='Введите k2')
inpEnt1 = Entry(width=20)
inpEnt2 = Entry(width=20)
res = Button(text='Вычслить')
inp3 = Label(text='result')
inp4 = Label(bg='black', width=30, fg='white')
inp1.grid(column=0, row=0)
inpEnt1.grid(column=1, row=0)
inpEnt2.grid(column=1, row=1)
inp2.grid(column=0, row=1)
inp3.grid(column=0, row=2)
inp4.grid(column=1, row=2, columnspan=2)
res.grid(column=2, row=0, rowspan=2)


def calc(event):
    k1 = float(inpEnt1.get())
    k2 = float(inpEnt2.get())
    for c in range(-3, 5 + 1):
        Fc = ((3 * k1) ** 1 / 5 - c) / (2 * (math.tan(c + k2)) ** 3)
        array.append(float(Fc))
        inp4['text'] = array


res.bind('<Button-1>', calc)
root.mainloop()
