from openpyxl import load_workbook
from tkinter import *
from tkinter import messagebox

def save():
    fn='main.xlsx'
    wb=load_workbook(fn)
    ws=wb['data']
    data=(e.get(),lb['text'])
    ws.append(data)
    wb,save(fn)
    wb.close()
    messagebox.askokcancel('1','2')

root=Tk()
root.title('Test')
root.geometry('200x200')
root.resizable(0,0)
e=Entry(root)
e.pack()
lb=Label(root,text='1',font='Arial 15 bold')
lb.pack()
btn=Button(root,text='save',font='Arial 15 bold',command=save)
btn.pack()
root.mainloop()
