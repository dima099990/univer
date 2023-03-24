from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
import math

Form, Window = uic.loadUiType("form.ui")
app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()


form.lineEdit.setText("10")
form.lineEdit_2.setText("10000")
form.lineEdit_3.setText("150")


def calc():
    c0 = int(form.lineEdit.text())
    v = int(form.lineEdit_2.text())
    q = int(form.lineEdit_3.text())
    t = float(0)
    c = float(1)

    while c > 0.1:
        c = c0 * math.exp(-q * t / v)
        t = t + 0.5
    else:
        c = round(c, 3)
        form.label_7.setText(str(t)+"ч")
        form.label_8.setText(str(c)+"гр\л")


        print("Остаточное содержание хлорки: ", c)
        print("Прошедшее время : ", t, "ч.")

def clear():
    form.label_7.setText("")
    form.label_8.setText("")
    form.lineEdit.setText("")
    form.lineEdit_2.setText("")
    form.lineEdit_3.setText("")


form.pushButton.clicked.connect(calc)
form.pushButton_2.clicked.connect(clear)




app.exec_()
