#!/usr/bin/env python3
import rospy
from dynamic_reconfigure.server import Server
from dyn_rcfg0_pkg.cfg     import HelloConfig    # packageName.
# You will see error line above in MS Code which is fine
# The name HelloConfig is automatically generated by appending Config 
# to the 3rd argument in gen.generate in the cfg file

def callback(config, level):
    global freq, msg, stop_display
    freq = config.freq
    msg = config.message
    stop_display = config.stop_disp
    return config # this line is required for the server

def display_hi():
    while not rospy.is_shutdown():
        rate = rospy.Rate(freq) 
        if stop_display == False:
            print(f"{freq} {msg}")
        rate.sleep()

if __name__ == "__main__":
    rospy.init_node("dyn_rcfg0", anonymous = False)
    srv = Server(HelloConfig, callback)
    display_hi()
    rospy.spin()