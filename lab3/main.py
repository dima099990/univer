from tkinter import *

root = Tk()
root.title('Орлов Д.В. Лаб №3')
root.geometry('600x400')
text1 = Label(text="Введите X: ")
text2 = Label(text="Введите Y: ")
text3 = Label(text="Введите Z: ")
text1.grid(column=0, row=0)
text2.grid(column=0, row=1)
text3.grid(column=0, row=2)

X = Entry(width=20)
Y = Entry(width=20)
Z = Entry(width=20)
X.grid(column=1, row=0)
Y.grid(column=1, row=1)
Z.grid(column=1, row=2)

answer = Label(bg='black', fg='white', width=60)
answer.grid(column=1, row=4, columnspan=2)

calc = Button(text="Вычислить")
calc.grid(column=2, row=1)


def num1(event):
    x = int(X.get())
    y = int(Y.get())
    z = int(Z.get())

    if x == y:
        print("x=y")
        answer['text'] = 'x=y'
    elif y == z:
        print("y=z")
        answer['text'] = 'y=z'
    elif z == x:
        print("z=x")
        answer['text'] = 'z=x'
    else:
        print("Переменные:  X,Y,Z попарно не равны!")
        answer['text'] = 'Переменные:  X,Y,Z попарно не равны!'


calc.bind('<Button-1>', num1)
root.mainloop()
