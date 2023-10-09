#!/usr/bin/env python3

import add_path
import rospy
from my_robot_common.import_me_if_u_can import say_it_works as say_it_works_1
from other_robot_common.other_if_u_can import say_it_works as say_it_works_2

if __name__ == '__main__':
    rospy.init_node('testing_library')
    say_it_works_1()
    say_it_works_2()
    # rospy.spin()
