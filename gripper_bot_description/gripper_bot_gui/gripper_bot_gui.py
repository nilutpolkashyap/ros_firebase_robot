# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gripper_bot_gui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(337, 319)
        self.armSlider = QtWidgets.QSlider(Form)
        self.armSlider.setGeometry(QtCore.QRect(50, 130, 241, 41))
        self.armSlider.setMaximum(180)
        self.armSlider.setSingleStep(1)
        self.armSlider.setOrientation(QtCore.Qt.Horizontal)
        self.armSlider.setObjectName("armSlider")
        self.gripperSlider = QtWidgets.QSlider(Form)
        self.gripperSlider.setGeometry(QtCore.QRect(50, 240, 241, 41))
        self.gripperSlider.setMaximum(110)
        self.gripperSlider.setOrientation(QtCore.Qt.Horizontal)
        self.gripperSlider.setObjectName("gripperSlider")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(124, 85, 91, 31))
        self.label.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(0, 255, 255);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(110, 210, 121, 31))
        self.label_2.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(0, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(20, 10, 291, 41))
        self.label_3.setStyleSheet("font: 75 16pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(170, 255, 0);")
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "arm_joint"))
        self.label_2.setText(_translate("Form", "gripper_joint"))
        self.label_3.setText(_translate("Form", "    GRIPPER BOT GUI"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

