# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SLAE_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SLAE_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1422, 675)
        Dialog.setMinimumSize(QtCore.QSize(1422, 675))
        self.tableView = QtWidgets.QTableView(Dialog)
        self.tableView.setGeometry(QtCore.QRect(90, 110, 731, 241))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.tableView.setFont(font)
        self.tableView.setObjectName("tableView")
        self.tableView_2 = QtWidgets.QTableView(Dialog)
        self.tableView_2.setGeometry(QtCore.QRect(90, 420, 731, 201))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.tableView_2.setFont(font)
        self.tableView_2.setObjectName("tableView_2")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(880, 90, 221, 51))
        self.pushButton.setStyleSheet("color:white;\n"
"background-color:rgb(20,20,20);\n"
"border-radius:8px;")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(880, 160, 221, 51))
        self.pushButton_2.setStyleSheet("color:white;\n"
"background-color:rgb(20,20,20);\n"
"border-radius:8px;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(880, 220, 221, 51))
        self.pushButton_3.setStyleSheet("color:white;\n"
"background-color:rgb(20,20,20);\n"
"border-radius:8px;")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(880, 280, 221, 51))
        self.pushButton_4.setStyleSheet("color:white;\n"
"background-color:rgb(20,20,20);\n"
"border-radius:8px;")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(880, 340, 221, 61))
        self.pushButton_5.setStyleSheet("color:white;\n"
"background-color:rgb(20,20,20);\n"
"border-radius:8px;")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(Dialog)
        self.pushButton_6.setGeometry(QtCore.QRect(1150, 90, 211, 51))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("color:white;\n"
"background-color:red;\n"
"border-radius:8px;")
        self.pushButton_6.setObjectName("pushButton_6")
        self.radioButton = QtWidgets.QRadioButton(Dialog)
        self.radioButton.setGeometry(QtCore.QRect(900, 450, 191, 71))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_2.setGeometry(QtCore.QRect(1100, 450, 221, 61))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(1140, 185, 231, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(1140, 230, 251, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(1140, 310, 251, 31))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(1140, 280, 231, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(90, 380, 211, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(90, 60, 211, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "Добавить строку"))
        self.pushButton_2.setText(_translate("Dialog", "Удалить строку"))
        self.pushButton_3.setText(_translate("Dialog", "Добавить колонку"))
        self.pushButton_4.setText(_translate("Dialog", "Удалить колонку"))
        self.pushButton_5.setText(_translate("Dialog", "Вычислить"))
        self.pushButton_6.setText(_translate("Dialog", "Убрать все"))
        self.radioButton.setText(_translate("Dialog", "Гаусс"))
        self.radioButton_2.setText(_translate("Dialog", "Зейдель"))
        self.label.setText(_translate("Dialog", "Мак. итераций"))
        self.label_2.setText(_translate("Dialog", "Ошибка"))
        self.label_3.setText(_translate("Dialog", "Выходные значения"))
        self.label_4.setText(_translate("Dialog", "Входные значения"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_SLAE_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
