from tkinter import *

root = Tk()
A = Entry(width=20)

btn_ok = Button(text='Рассчитать')
btn_clear = Button(text='Очистить')
lbl = Label(bg='black', fg='white', width=80)
lbl2 = Label(bg='black', fg='white', width=80)
lbl3 = Label(bg='white', fg='white', width=80)
lbl4 = Label(bg='black', fg='white', width=80)
lbl4['text']=['Введите кол-во секунд']


def ok(event):
    a = int(A.get())
    while a >= 3601:
        a = a - 3600
    lbl['text'] = 'Кол-во секунд с начала прошлого часа ' + str(a)
    lbl2['text'] = "Целые минуты с начала последнего часа:" + str(int(a / 60))

def clear(event):
    lbl['text']=''
    lbl2['text'] = ''


btn_ok.bind('<Button-1>', ok)
btn_clear.bind('<Button-1>',clear)
lbl4.pack()
A.pack()
btn_ok.pack()

lbl.pack()
lbl3.pack()
lbl2.pack()
btn_clear.pack()
root.mainloop()