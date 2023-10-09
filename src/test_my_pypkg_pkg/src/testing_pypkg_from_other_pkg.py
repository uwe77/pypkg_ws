#!/usr/bin/env python3

import add_path
import rospy
from my_robot_common.import_me_if_u_can import say_it_works
from other_robot_common.other_if_u_can import say_it_works as other_if_u_can
if __name__ == '__main__':
    rospy.init_node('testing_library')
    print('from testing_pypkg_from_other_pkg.py')
    say_it_works()
    other_if_u_can()
    # rospy.spin()
