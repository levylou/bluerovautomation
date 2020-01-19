execute_process(COMMAND "/home/levy/Schreibtisch/bluerov_auto/build/bluerov_ros_playground/catkin_generated/python_distutils_install.sh" RESULT_VARIABLE res)

if(NOT res EQUAL 0)
  message(FATAL_ERROR "execute_process(/home/levy/Schreibtisch/bluerov_auto/build/bluerov_ros_playground/catkin_generated/python_distutils_install.sh) returned error code ")
endif()
