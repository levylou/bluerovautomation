# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "bluerov_ros_playground: 1 messages, 0 services")

set(MSG_I_FLAGS "-Ibluerov_ros_playground:/home/levy/Schreibtisch/bluerov_auto/src/bluerov_ros_playground/msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(bluerov_ros_playground_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/levy/Schreibtisch/bluerov_auto/src/bluerov_ros_playground/msg/Custom.msg" NAME_WE)
add_custom_target(_bluerov_ros_playground_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "bluerov_ros_playground" "/home/levy/Schreibtisch/bluerov_auto/src/bluerov_ros_playground/msg/Custom.msg" ""
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(bluerov_ros_playground
  "/home/levy/Schreibtisch/bluerov_auto/src/bluerov_ros_playground/msg/Custom.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/bluerov_ros_playground
)

### Generating Services

### Generating Module File
_generate_module_cpp(bluerov_ros_playground
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/bluerov_ros_playground
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(bluerov_ros_playground_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(bluerov_ros_playground_generate_messages bluerov_ros_playground_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/levy/Schreibtisch/bluerov_auto/src/bluerov_ros_playground/msg/Custom.msg" NAME_WE)
add_dependencies(bluerov_ros_playground_generate_messages_cpp _bluerov_ros_playground_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(bluerov_ros_playground_gencpp)
add_dependencies(bluerov_ros_playground_gencpp bluerov_ros_playground_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS bluerov_ros_playground_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages
_generate_msg_eus(bluerov_ros_playground
  "/home/levy/Schreibtisch/bluerov_auto/src/bluerov_ros_playground/msg/Custom.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/bluerov_ros_playground
)

### Generating Services

### Generating Module File
_generate_module_eus(bluerov_ros_playground
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/bluerov_ros_playground
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(bluerov_ros_playground_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(bluerov_ros_playground_generate_messages bluerov_ros_playground_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/levy/Schreibtisch/bluerov_auto/src/bluerov_ros_playground/msg/Custom.msg" NAME_WE)
add_dependencies(bluerov_ros_playground_generate_messages_eus _bluerov_ros_playground_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(bluerov_ros_playground_geneus)
add_dependencies(bluerov_ros_playground_geneus bluerov_ros_playground_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS bluerov_ros_playground_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(bluerov_ros_playground
  "/home/levy/Schreibtisch/bluerov_auto/src/bluerov_ros_playground/msg/Custom.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/bluerov_ros_playground
)

### Generating Services

### Generating Module File
_generate_module_lisp(bluerov_ros_playground
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/bluerov_ros_playground
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(bluerov_ros_playground_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(bluerov_ros_playground_generate_messages bluerov_ros_playground_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/levy/Schreibtisch/bluerov_auto/src/bluerov_ros_playground/msg/Custom.msg" NAME_WE)
add_dependencies(bluerov_ros_playground_generate_messages_lisp _bluerov_ros_playground_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(bluerov_ros_playground_genlisp)
add_dependencies(bluerov_ros_playground_genlisp bluerov_ros_playground_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS bluerov_ros_playground_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages
_generate_msg_nodejs(bluerov_ros_playground
  "/home/levy/Schreibtisch/bluerov_auto/src/bluerov_ros_playground/msg/Custom.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/bluerov_ros_playground
)

### Generating Services

### Generating Module File
_generate_module_nodejs(bluerov_ros_playground
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/bluerov_ros_playground
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(bluerov_ros_playground_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(bluerov_ros_playground_generate_messages bluerov_ros_playground_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/levy/Schreibtisch/bluerov_auto/src/bluerov_ros_playground/msg/Custom.msg" NAME_WE)
add_dependencies(bluerov_ros_playground_generate_messages_nodejs _bluerov_ros_playground_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(bluerov_ros_playground_gennodejs)
add_dependencies(bluerov_ros_playground_gennodejs bluerov_ros_playground_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS bluerov_ros_playground_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(bluerov_ros_playground
  "/home/levy/Schreibtisch/bluerov_auto/src/bluerov_ros_playground/msg/Custom.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/bluerov_ros_playground
)

### Generating Services

### Generating Module File
_generate_module_py(bluerov_ros_playground
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/bluerov_ros_playground
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(bluerov_ros_playground_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(bluerov_ros_playground_generate_messages bluerov_ros_playground_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/levy/Schreibtisch/bluerov_auto/src/bluerov_ros_playground/msg/Custom.msg" NAME_WE)
add_dependencies(bluerov_ros_playground_generate_messages_py _bluerov_ros_playground_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(bluerov_ros_playground_genpy)
add_dependencies(bluerov_ros_playground_genpy bluerov_ros_playground_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS bluerov_ros_playground_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/bluerov_ros_playground)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/bluerov_ros_playground
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/bluerov_ros_playground)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/bluerov_ros_playground
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/bluerov_ros_playground)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/bluerov_ros_playground
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/bluerov_ros_playground)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/bluerov_ros_playground
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/bluerov_ros_playground)
  install(CODE "execute_process(COMMAND \"/usr/bin/python2\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/bluerov_ros_playground\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/bluerov_ros_playground
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
