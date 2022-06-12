from PyQt5 import QtWidgets, uic, QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication, QLCDNumber, QProgressBar, QLabel, QComboBox, QPushButton, QSlider
from PyQt5.QtCore import QTime, QTimer
import sys
import pyrebase
import time
from PyQt5.QtWidgets import (QApplication, QWidget)
from PyQt5.Qt import Qt

firebaseConfig= {
    "apiKey": "*************************************",
    "authDomain": "*************************************",
    "databaseURL": "*************************************",
    "projectId": "*************************************",
    "storageBucket": "*************************************",
    "messagingSenderId": "*************************************",
    "appId": "*************************************"
}

firebase = pyrebase.initialize_app(firebaseConfig)

db = firebase.database()


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('remote_gui_ros.ui', self)

        self.setWindowIcon(QtGui.QIcon('images/icon.png'))
        # set the title
        self.setWindowTitle("Icon")

        self.arm = self.findChild(QSlider, "arm_slider")
        self.arm.valueChanged.connect(self.change_angle)

        self.front_button = self.findChild(QPushButton, "front_button")
        self.front_button.clicked.connect(self.front_button_clicked)

        self.back_button = self.findChild(QPushButton, "back_button")
        self.back_button.clicked.connect(self.back_button_clicked)

        self.stop_button = self.findChild(QPushButton, "stop_button")
        self.stop_button.clicked.connect(self.stop_button_clicked)

        self.left_button = self.findChild(QPushButton, "left_button")
        self.left_button.clicked.connect(self.left_button_clicked)

        self.right_button = self.findChild(QPushButton, "right_button")
        self.right_button.clicked.connect(self.right_button_clicked)

        self.lturn_button = self.findChild(QPushButton, "left_turn_button")
        self.lturn_button.clicked.connect(self.lturn_button_clicked)

        self.rturn_button = self.findChild(QPushButton, "right_turn_button")
        self.rturn_button.clicked.connect(self.rturn_button_clicked)

        self.back_button = self.findChild(QPushButton, "zig_zag_button")
        self.back_button.clicked.connect(self.zig_zag_button_clicked)

        self.show()

    def clickme(self):
        global light_status
        light_status = not light_status
        if(light_status == True):
            db.child("test").update({"light": 1})
            print("LIGHT ON")
        else:
            db.child("test").update({"light": 0})
            print("LIGHT OFF")

    def front_button_clicked(self):
        db.child("test").update({"command": "FR"})
        print("GO FRONT")

    def back_button_clicked(self):
        db.child("test").update({"command": "BK"})
        print("GO BACK")

    def stop_button_clicked(self):
        db.child("test").update({"command": "ST"})
        print("STOP")

    def left_button_clicked(self):
        db.child("test").update({"command": "LR"})
        print("LEFT ROTATE")

    def right_button_clicked(self):
        db.child("test").update({"command": "RR"})
        print("RIGHT ROTATE")

    def lturn_button_clicked(self):
        db.child("test").update({"command": "LT"})
        print("LEFT TURN")

    def rturn_button_clicked(self):
        db.child("test").update({"command": "RT"})
        print("RIGHT TURN")

    def zig_zag_button_clicked(self):
        db.child("test").update({"command": "ZIGZAG"})
        print("GO ZIGZAG")

    def change_angle(self, value):
        # Change font size of label. Size value could
        # be anything consistent with the dimension of label.
        db.child("test").update({"arm": value})
        print(value)


app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()