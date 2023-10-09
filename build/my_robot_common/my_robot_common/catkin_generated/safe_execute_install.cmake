execute_process(COMMAND "/home/uwe/pypkg_ws/build/my_robot_common/my_robot_common/catkin_generated/python_distutils_install.sh" RESULT_VARIABLE res)

if(NOT res EQUAL 0)
  message(FATAL_ERROR "execute_process(/home/uwe/pypkg_ws/build/my_robot_common/my_robot_common/catkin_generated/python_distutils_install.sh) returned error code ")
endif()
