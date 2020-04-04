'''
===============================================================================
Program Description 
	This program takes input from the joystick and returns normalised speeds 
    for each driving motor

Author:         Jehan Shah, jehan.shah8@gmail.com
Maintainer:     Jehan Shah, jehan.shah8@gmail.com
Version:        March 31, 2020
Status:         In progress
===============================================================================
'''
#!/usr/bin/env python
import rospy
from std_msgs.msg import String

#listen from joy
def something():
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("chatter", String, callback)

#publish speeds
def rescale() {

}

def teleop_drive():
    pub = rospy.Publisher()