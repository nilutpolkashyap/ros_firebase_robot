import pyrebase
import time
# from PyQt5 import QtCore, QtGui, QtWidgets
import rospy
from std_msgs.msg import Float64
from geometry_msgs.msg import Twist

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

count = 0

pubslide1 = rospy.Publisher('/gripper_bot/gripper_joint_position_controller/command',Float64,queue_size=1)
pubslide2 = rospy.Publisher('/gripper_bot/arm_joint_position_controller/command',Float64,queue_size=1)
rospy.init_node('ROScontrol', anonymous=True)

velocity_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
vel_msg = Twist()

while True:
    arm_control = db.child("test").child("arm").get().val()

    if arm_control == 0:
        print(1)
        pubslide1.publish(0.01)
    elif arm_control == 1:
        print(76)
        pubslide1.publish(0.76)
    elif arm_control == 2:
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

    elif direction == "BK":
        print("BACK")
        vel_msg.linear.x = -0.5
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
