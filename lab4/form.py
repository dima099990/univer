# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainwidow(object):
    def setupUi(self, mainwidow):
        mainwidow.setObjectName("mainwidow")
        mainwidow.resize(292, 363)
        self.centralwidget = QtWidgets.QWidget(mainwidow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(50, 270, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 0, 261, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 210, 141, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 240, 141, 20))
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 100, 211, 20))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 140, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(10, 180, 113, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 80, 241, 16))
        self.label_4.setTextFormat(QtCore.Qt.AutoText)
        self.label_4.setScaledContents(False)
        self.label_4.setWordWrap(False)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 120, 141, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 160, 151, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(170, 210, 81, 16))
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(170, 240, 81, 16))
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(50, 300, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        mainwidow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(mainwidow)
        self.statusbar.setObjectName("statusbar")
        mainwidow.setStatusBar(self.statusbar)

        self.retranslateUi(mainwidow)
        QtCore.QMetaObject.connectSlotsByName(mainwidow)

    def retranslateUi(self, mainwidow):
        _translate = QtCore.QCoreApplication.translate
        mainwidow.setWindowTitle(_translate("mainwidow", "MainWindow"))
        self.pushButton.setText(_translate("mainwidow", "Вычислить"))
        self.label.setText(_translate("mainwidow", "формула расчета: С=С0е-Qt/V где t-время, С0-начальная концентрация"))
        self.label_2.setText(_translate("mainwidow", "Прошедшее время"))
        self.label_3.setText(_translate("mainwidow", "Остаточная концентрация"))
        self.label_4.setText(_translate("mainwidow", "Введите изначальное содержание хлорки"))
        self.label_5.setText(_translate("mainwidow", "Объем воды"))
        self.label_6.setText(_translate("mainwidow", "Скорость потока воды"))
        self.pushButton_2.setText(_translate("mainwidow", "Очистить"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainwidow = QtWidgets.QMainWindow()
    ui = Ui_mainwidow()
    ui.setupUi(mainwidow)
    mainwidow.show()
    sys.exit(app.exec_())