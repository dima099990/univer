from tkinter import *
import numpy as np
win=Tk()
win.title('ВИ12 Орлов')
#win.geometry('400x400+200+200')

x11=7.3
x12=-8.1
x13=12.7
x14=-6.7

x21=0.5
x22=6.2
x23=-8.3
x24=9.2

x31=8.2
x32=-5.4
x33=4.3
x34=-2.5

x41=2.4
x42=1.5
x43=3.3
x44=4.2

b1=8.8
b2=21.5
b3=6.2
b4=-6.2

def calc():
    A = np.array([[x11/2,x12*2,x13/1.2,x14*0.9],[x21/2,x22*2,x23/1.2,x24*0.9],[x31/2,x32*2,x33/1.2,x34*0.9],[x41/2,x42*2,x43/1.2,x44*0.9]])
    b = np.array([b1,b2,b3,b4])
    x = np.linalg.solve(A, b)
    z='x1= {:.2f}'.format(x[0]),'x2= {:.2f}'.format(x[1]),'x3= {:.2f}'.format(x[2]),'x4= {:.2f}'.format(x[3])
    result['text']=z
    pr1=x11/2*x[0]+x12*2*x[1]+x13/1.2*x[2]+x14*0.9*x[3]
    pr2=x21/2*x[0]+x22*2*x[1]+x23/1.2*x[2]+x24*0.9*x[3]
    pr3=x31/2*x[0]+x32*2*x[1]+x33/1.2*x[2]+x34*0.9*x[3]
    pr4=x41/2*x[0]+x42*2*x[1]+x43/1.2*x[2]+x44*0.9*x[3]
    proverka['text']=pr1,pr2,pr3,pr4

btn=Button(text='Вычислить',command=calc)
btn.grid(column=0,row=0)
result=Label(text='')
result.grid(column=0,row=1)
proverka=Label(text='')
proverka.grid(column=0,row=2)

win.mainloop()
