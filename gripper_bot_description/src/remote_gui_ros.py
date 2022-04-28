from PyQt5 import QtWidgets, uic, QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication, QLCDNumber, QProgressBar, QLabel, QComboBox, QPushButton, QSlider
from PyQt5.QtCore import QTime, QTimer
import sys
import pyrebase
import time
from PyQt5.QtWidgets import (QApplication, QWidget)
from PyQt5.Qt import Qt

firebaseConfig= {
    "apiKey": "AIzaSyDJ4JZTKlyqcLSD921BkVjZHMB3jUqa4eQ",
    "authDomain": "phoenix-94e5f.firebaseapp.com",
    "databaseURL": "https://phoenix-94e5f.firebaseio.com",
    "projectId": "phoenix-94e5f",
    "storageBucket": "phoenix-94e5f.appspot.com",
    "messagingSenderId": "918478582882",
    "appId": "1:918478582882:web:8cde319e61b1de7cb30d3b"
}

firebase=pyrebase.initialize_app(firebaseConfig)

db=firebase.database()

light_status = True

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('remote_gui_ros.ui', self)

        self.setWindowIcon(QtGui.QIcon('images/icon.png'))
        # set the title
        self.setWindowTitle("Icon")

        self.arm = self.findChild(QSlider, "arm_slider")
        self.arm.setToolTip("CONTROL ARM")
        self.arm.valueChanged.connect(self.change_angle)

        self.keyboard = self.findChild(QPushButton, "keyboard_button")
        self.keyboard.setToolTip('W - Go Front\nX - Go Back\nD - Right Rotate\nA - Left Rotate\nQ - Left Turn\nE - Right Turn\n↑ ↓ - Arm Control')
        self.keyboard.setToolTipDuration(50000)

        # self.light = self.findChild(QPushButton, "light_button")
        # self.light.setToolTip("TURN LIGHT ON/OFF")
        # self.light.clicked.connect(self.clickme)

        self.front_button = self.findChild(QPushButton, "front_button")
        self.front_button.setToolTip("GO FRONT")
        self.front_button.clicked.connect(self.front_button_clicked)

        self.back_button = self.findChild(QPushButton, "back_button")
        self.back_button.setToolTip("GO BACK")
        self.back_button.clicked.connect(self.back_button_clicked)

        self.stop_button = self.findChild(QPushButton, "stop_button")
        self.stop_button.setToolTip("STOP")
        self.stop_button.clicked.connect(self.stop_button_clicked)

        self.left_button = self.findChild(QPushButton, "left_button")
        self.left_button.setToolTip("LEFT ROTATE")
        self.left_button.clicked.connect(self.left_button_clicked)

        self.right_button = self.findChild(QPushButton, "right_button")
        self.right_button.setToolTip("RIGHT ROTATE")
        self.right_button.clicked.connect(self.right_button_clicked)

        self.lturn_button = self.findChild(QPushButton, "left_turn_button")
        self.lturn_button.setToolTip("LEFT TURN")
        self.lturn_button.clicked.connect(self.lturn_button_clicked)

        self.rturn_button = self.findChild(QPushButton, "right_turn_button")
        self.rturn_button.setToolTip("RIGHT TURN")
        self.rturn_button.clicked.connect(self.rturn_button_clicked)

        self.show()

    def clickme(self):
        global light_status
        light_status = not light_status
        if(light_status == True):
            db.child("test").update({"light":1})
            print("LIGHT ON")
        else:
            db.child("test").update({"light":0})
            print("LIGHT OFF")

    def front_button_clicked(self):
        db.child("test").update({"command":"FR"})
        print("GO FRONT")

    def back_button_clicked(self):
        db.child("test").update({"command":"BK"})
        print("GO BACK")

    def stop_button_clicked(self):
        db.child("test").update({"command":"ST"})
        print("STOP")

    def left_button_clicked(self):
        db.child("test").update({"command":"LR"})
        print("LEFT ROTATE")

    def right_button_clicked(self):
        db.child("test").update({"command":"RR"})
        print("RIGHT ROTATE")

    def lturn_button_clicked(self):
        db.child("test").update({"command":"LT"})
        print("LEFT TURN")

    def rturn_button_clicked(self):
        db.child("test").update({"command":"RT"})
        print("RIGHT TURN")

    def change_angle(self, value):
        # Change font size of label. Size value could 
        # be anything consistent with the dimension of label.
        db.child("test").update({"arm":value})
        print(value)


    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Q:
            db.child("test").update({"command":"LT"})
            print("LEFT TURN")
            # self.test_method()
        if event.key() == Qt.Key_W:
            db.child("test").update({"command":"FR"})
            print("GO FRONT")
        if event.key() == Qt.Key_E:
            db.child("test").update({"command":"RT"})
            print("RIGHT TURN")
        if event.key() == Qt.Key_A:
            db.child("test").update({"command":"LR"})
            print("LEFT ROTATE")
        if event.key() == Qt.Key_S:
            db.child("test").update({"command":"ST"})
            print("STOP")
        if event.key() == Qt.Key_D:
            db.child("test").update({"command":"RR"})
            print("RIGHT ROTATE")
        if event.key() == Qt.Key_X:
            db.child("test").update({"command":"BK"})
            print("GO BACK")
        # if event.key() == Qt.Key_L:
        #     global light_status
        #     light_status = not light_status
        #     if(light_status == True):
        #         db.child("test").update({"light":1})
        #         print("LIGHT ON")
        #     else:
        #         db.child("test").update({"light":0})
        #         print("LIGHT OFF")

    # def test_method(self):
    #     print('Q pressed')

app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()
