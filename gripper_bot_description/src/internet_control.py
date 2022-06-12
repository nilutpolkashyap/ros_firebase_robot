import pyrebase
import time
# from PyQt5 import QtCore, QtGui, QtWidgets
import rospy
from std_msgs.msg import Float64
from geometry_msgs.msg import Twist

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

count = 0

pubslide1 = rospy.Publisher(
    '/gripper_bot/gripper_joint_position_controller/command', Float64, queue_size=1)
pubslide2 = rospy.Publisher(
    '/gripper_bot/arm_joint_position_controller/command', Float64, queue_size=1)
rospy.init_node('ROScontrol', anonymous=True)

velocity_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
vel_msg = Twist()

while True:
    arm_control = db.child("test").child("arm").get().val()

    if arm_control == 0:
        print(1)
        pubslide1.publish(0.01)
    elif arm_control == 1:
        print(19)
        pubslide1.publish(0.19)
    elif arm_control == 2:
        print(38)
        pubslide1.publish(0.38)
    elif arm_control == 3:
        print(57)
        pubslide1.publish(0.57)
    elif arm_control == 4:
        print(77)
        pubslide1.publish(0.77)
    elif arm_control == 5:
        print(96)
        pubslide1.publish(0.96)
    elif arm_control == 6:
        print(115)
        pubslide1.publish(1.15)
    elif arm_control == 7:
        print(135)
        pubslide1.publish(1.35)
    elif arm_control == 8:
        print(157)
        pubslide1.publish(1.57)
    # print(count, users)
    # time.sleep(.5)
    # count = count + 1

    direction = db.child("test").child("command").get().val()

    if direction == "FR":
        print("FRONT")
        vel_msg.linear.x = 0.5
        vel_msg.linear.y = 0
        vel_msg.linear.z = 0
        vel_msg.angular.x = 0
        vel_msg.angular.y = 0
        vel_msg.angular.z = 0
        velocity_publisher.publish(vel_msg)

    elif direction == "ST":
        print("STOP")
        vel_msg.linear.x = 0
        vel_msg.linear.y = 0
        vel_msg.linear.z = 0
        vel_msg.angular.x = 0
        vel_msg.angular.y = 0
        vel_msg.angular.z = 0
        velocity_publisher.publish(vel_msg)

    elif direction == "LR":
        print("LEFT ROTATE")
        vel_msg.linear.x = 0
        vel_msg.linear.y = 0
        vel_msg.linear.z = 0
        vel_msg.angular.x = 0
        vel_msg.angular.y = 0
        vel_msg.angular.z = 3.0
        velocity_publisher.publish(vel_msg)

    elif direction == "RR":
        print("RIGHT ROTATE")
        vel_msg.linear.x = 0
        vel_msg.linear.y = 0
        vel_msg.linear.z = 0
        vel_msg.angular.x = 0
        vel_msg.angular.y = 0
        vel_msg.angular.z = -3.0
        velocity_publisher.publish(vel_msg)

    elif direction == "LT":
        print("LEFT TURN")
        vel_msg.linear.x = 0.5
        vel_msg.linear.y = 0
        vel_msg.linear.z = 0
        vel_msg.angular.x = 0
        vel_msg.angular.y = 0
        vel_msg.angular.z = 1.0
        velocity_publisher.publish(vel_msg)

    elif direction == "RT":
        print("RIGHT TURN")
        vel_msg.linear.x = 0.5
        vel_msg.linear.y = 0
        vel_msg.linear.z = 0
        vel_msg.angular.x = 0
        vel_msg.angular.y = 0
        vel_msg.angular.z = -1.0
        velocity_publisher.publish(vel_msg)

    elif direction == "BK":
        print("BACK")
        vel_msg.linear.x = -0.5
        vel_msg.linear.y = 0
        vel_msg.linear.z = 0
        vel_msg.angular.x = 0
        vel_msg.angular.y = 0
        vel_msg.angular.z = 0
        velocity_publisher.publish(vel_msg)

    elif direction == "ZIGZAG":
        print("ZIGZAG")
        vel_msg.linear.x = 0.5
        vel_msg.linear.y = 0
        vel_msg.linear.z = 0
        vel_msg.angular.x = 0
        vel_msg.angular.y = 0
        vel_msg.angular.z = 3.0
        velocity_publisher.publish(vel_msg)
        time.sleep(2.5)
        vel_msg.linear.x = 0.5
        vel_msg.linear.y = 0
        vel_msg.linear.z = 0
        vel_msg.angular.x = 0
        vel_msg.angular.y = 0
        vel_msg.angular.z = -3.0
        velocity_publisher.publish(vel_msg)
        time.sleep(2.5)