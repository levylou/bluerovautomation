# Install script for directory: /home/levy/Schreibtisch/bluerov_auto/src/bluerov_ros_playground

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/levy/Schreibtisch/bluerov_auto/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  include("/home/levy/Schreibtisch/bluerov_auto/build/bluerov_ros_playground/catkin_generated/safe_execute_install.cmake")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/bluerov_ros_playground/msg" TYPE FILE FILES "/home/levy/Schreibtisch/bluerov_auto/src/bluerov_ros_playground/msg/Custom.msg")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/bluerov_ros_playground/cmake" TYPE FILE FILES "/home/levy/Schreibtisch/bluerov_auto/build/bluerov_ros_playground/catkin_generated/installspace/bluerov_ros_playground-msg-paths.cmake")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include" TYPE DIRECTORY FILES "/home/levy/Schreibtisch/bluerov_auto/devel/include/bluerov_ros_playground")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/roseus/ros" TYPE DIRECTORY FILES "/home/levy/Schreibtisch/bluerov_auto/devel/share/roseus/ros/bluerov_ros_playground")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/common-lisp/ros" TYPE DIRECTORY FILES "/home/levy/Schreibtisch/bluerov_auto/devel/share/common-lisp/ros/bluerov_ros_playground")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/gennodejs/ros" TYPE DIRECTORY FILES "/home/levy/Schreibtisch/bluerov_auto/devel/share/gennodejs/ros/bluerov_ros_playground")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  execute_process(COMMAND "/usr/bin/python2" -m compileall "/home/levy/Schreibtisch/bluerov_auto/devel/lib/python2.7/dist-packages/bluerov_ros_playground")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages" TYPE DIRECTORY FILES "/home/levy/Schreibtisch/bluerov_auto/devel/lib/python2.7/dist-packages/bluerov_ros_playground")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/levy/Schreibtisch/bluerov_auto/build/bluerov_ros_playground/catkin_generated/installspace/bluerov_ros_playground.pc")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/bluerov_ros_playground/cmake" TYPE FILE FILES "/home/levy/Schreibtisch/bluerov_auto/build/bluerov_ros_playground/catkin_generated/installspace/bluerov_ros_playground-msg-extras.cmake")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/bluerov_ros_playground/cmake" TYPE FILE FILES
    "/home/levy/Schreibtisch/bluerov_auto/build/bluerov_ros_playground/catkin_generated/installspace/bluerov_ros_playgroundConfig.cmake"
    "/home/levy/Schreibtisch/bluerov_auto/build/bluerov_ros_playground/catkin_generated/installspace/bluerov_ros_playgroundConfig-version.cmake"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/bluerov_ros_playground" TYPE FILE FILES "/home/levy/Schreibtisch/bluerov_auto/src/bluerov_ros_playground/package.xml")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/levy/Schreibtisch/bluerov_auto/build/bluerov_ros_playground/catkin_generated/installspace/bluerov_ros_playground.pc")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/bluerov_ros_playground/cmake" TYPE FILE FILES "/home/levy/Schreibtisch/bluerov_auto/build/bluerov_ros_playground/catkin_generated/installspace/bluerov_ros_playground-msg-extras.cmake")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/bluerov_ros_playground/cmake" TYPE FILE FILES
    "/home/levy/Schreibtisch/bluerov_auto/build/bluerov_ros_playground/catkin_generated/installspace/bluerov_ros_playgroundConfig.cmake"
    "/home/levy/Schreibtisch/bluerov_auto/build/bluerov_ros_playground/catkin_generated/installspace/bluerov_ros_playgroundConfig-version.cmake"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/bluerov_ros_playground" TYPE FILE FILES "/home/levy/Schreibtisch/bluerov_auto/src/bluerov_ros_playground/package.xml")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/bluerov_ros_playground/launch" TYPE FILE FILES
    "/home/levy/Schreibtisch/bluerov_auto/src/bluerov_ros_playground/launch/gazebo.launch"
    "/home/levy/Schreibtisch/bluerov_auto/src/bluerov_ros_playground/launch/gazebo_teleop.launch"
    "/home/levy/Schreibtisch/bluerov_auto/src/bluerov_ros_playground/launch/gazebo_sitl.launch"
    "/home/levy/Schreibtisch/bluerov_auto/src/bluerov_ros_playground/launch/rviz.launch"
    "/home/levy/Schreibtisch/bluerov_auto/src/bluerov_ros_playground/launch/mav_pluginlists.yaml"
    "/home/levy/Schreibtisch/bluerov_auto/src/bluerov_ros_playground/launch/user_mav.launch"
    "/home/levy/Schreibtisch/bluerov_auto/src/bluerov_ros_playground/launch/video.launch"
    "/home/levy/Schreibtisch/bluerov_auto/src/bluerov_ros_playground/launch/bluerov2_node.launch"
    "/home/levy/Schreibtisch/bluerov_auto/src/bluerov_ros_playground/launch/send_depth.launch"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/bluerov_ros_playground" TYPE DIRECTORY FILES
    "/home/levy/Schreibtisch/bluerov_auto/src/bluerov_ros_playground/model"
    "/home/levy/Schreibtisch/bluerov_auto/src/bluerov_ros_playground/config"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/bluerov_ros_playground" TYPE PROGRAM FILES "/home/levy/Schreibtisch/bluerov_auto/build/bluerov_ros_playground/catkin_generated/installspace/user_mav")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/bluerov_ros_playground" TYPE PROGRAM FILES "/home/levy/Schreibtisch/bluerov_auto/build/bluerov_ros_playground/catkin_generated/installspace/video")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/bluerov_ros_playground" TYPE PROGRAM FILES "/home/levy/Schreibtisch/bluerov_auto/build/bluerov_ros_playground/catkin_generated/installspace/gazebo_teleop.py")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/bluerov_ros_playground" TYPE PROGRAM FILES "/home/levy/Schreibtisch/bluerov_auto/build/bluerov_ros_playground/catkin_generated/installspace/sitl.py")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/bluerov_ros_playground" TYPE PROGRAM FILES "/home/levy/Schreibtisch/bluerov_auto/build/bluerov_ros_playground/catkin_generated/installspace/send_depth.py")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/bluerov_ros_playground" TYPE PROGRAM FILES "/home/levy/Schreibtisch/bluerov_auto/build/bluerov_ros_playground/catkin_generated/installspace/bridge.py")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/bluerov_ros_playground" TYPE PROGRAM FILES "/home/levy/Schreibtisch/bluerov_auto/build/bluerov_ros_playground/catkin_generated/installspace/bluerov_node.py")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/bluerov_ros_playground" TYPE PROGRAM FILES "/home/levy/Schreibtisch/bluerov_auto/build/bluerov_ros_playground/catkin_generated/installspace/control.py")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/bluerov_ros_playground" TYPE PROGRAM FILES "/home/levy/Schreibtisch/bluerov_auto/build/bluerov_ros_playground/catkin_generated/installspace/joystick.py")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/bluerov_ros_playground" TYPE PROGRAM FILES "/home/levy/Schreibtisch/bluerov_auto/build/bluerov_ros_playground/catkin_generated/installspace/autonomous.py")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/bluerov_ros_playground" TYPE PROGRAM FILES "/home/levy/Schreibtisch/bluerov_auto/build/bluerov_ros_playground/catkin_generated/installspace/node")
endif()

