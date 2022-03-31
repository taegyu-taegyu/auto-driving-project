# Install script for directory: /home/kw-cobot/wego_ws/auto-driving-project/src

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/kw-cobot/wego_ws/auto-driving-project/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "Releas")
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
  
      if (NOT EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}")
        file(MAKE_DIRECTORY "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}")
      endif()
      if (NOT EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/.catkin")
        file(WRITE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/.catkin" "")
      endif()
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/home/kw-cobot/wego_ws/auto-driving-project/install/_setup_util.py")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
file(INSTALL DESTINATION "/home/kw-cobot/wego_ws/auto-driving-project/install" TYPE PROGRAM FILES "/home/kw-cobot/wego_ws/auto-driving-project/build/catkin_generated/installspace/_setup_util.py")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/home/kw-cobot/wego_ws/auto-driving-project/install/env.sh")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
file(INSTALL DESTINATION "/home/kw-cobot/wego_ws/auto-driving-project/install" TYPE PROGRAM FILES "/home/kw-cobot/wego_ws/auto-driving-project/build/catkin_generated/installspace/env.sh")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/home/kw-cobot/wego_ws/auto-driving-project/install/setup.bash;/home/kw-cobot/wego_ws/auto-driving-project/install/local_setup.bash")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
file(INSTALL DESTINATION "/home/kw-cobot/wego_ws/auto-driving-project/install" TYPE FILE FILES
    "/home/kw-cobot/wego_ws/auto-driving-project/build/catkin_generated/installspace/setup.bash"
    "/home/kw-cobot/wego_ws/auto-driving-project/build/catkin_generated/installspace/local_setup.bash"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/home/kw-cobot/wego_ws/auto-driving-project/install/setup.sh;/home/kw-cobot/wego_ws/auto-driving-project/install/local_setup.sh")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
file(INSTALL DESTINATION "/home/kw-cobot/wego_ws/auto-driving-project/install" TYPE FILE FILES
    "/home/kw-cobot/wego_ws/auto-driving-project/build/catkin_generated/installspace/setup.sh"
    "/home/kw-cobot/wego_ws/auto-driving-project/build/catkin_generated/installspace/local_setup.sh"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/home/kw-cobot/wego_ws/auto-driving-project/install/setup.zsh;/home/kw-cobot/wego_ws/auto-driving-project/install/local_setup.zsh")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
file(INSTALL DESTINATION "/home/kw-cobot/wego_ws/auto-driving-project/install" TYPE FILE FILES
    "/home/kw-cobot/wego_ws/auto-driving-project/build/catkin_generated/installspace/setup.zsh"
    "/home/kw-cobot/wego_ws/auto-driving-project/build/catkin_generated/installspace/local_setup.zsh"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/home/kw-cobot/wego_ws/auto-driving-project/install/.rosinstall")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
file(INSTALL DESTINATION "/home/kw-cobot/wego_ws/auto-driving-project/install" TYPE FILE FILES "/home/kw-cobot/wego_ws/auto-driving-project/build/catkin_generated/installspace/.rosinstall")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for each subdirectory.
  include("/home/kw-cobot/wego_ws/auto-driving-project/build/hector_slam/hector_geotiff_launch/cmake_install.cmake")
  include("/home/kw-cobot/wego_ws/auto-driving-project/build/hector_slam/hector_slam/cmake_install.cmake")
  include("/home/kw-cobot/wego_ws/auto-driving-project/build/hector_slam/hector_slam_launch/cmake_install.cmake")
  include("/home/kw-cobot/wego_ws/auto-driving-project/build/navigation/navigation/cmake_install.cmake")
  include("/home/kw-cobot/wego_ws/auto-driving-project/build/realsense-ros/realsense2_description/cmake_install.cmake")
  include("/home/kw-cobot/wego_ws/auto-driving-project/build/hector_slam/hector_map_tools/cmake_install.cmake")
  include("/home/kw-cobot/wego_ws/auto-driving-project/build/hector_slam/hector_nav_msgs/cmake_install.cmake")
  include("/home/kw-cobot/wego_ws/auto-driving-project/build/scout_ros/scout_msgs/cmake_install.cmake")
  include("/home/kw-cobot/wego_ws/auto-driving-project/build/teleop_twist_keyboard/cmake_install.cmake")
  include("/home/kw-cobot/wego_ws/auto-driving-project/build/turtlebot3/turtlebot3/cmake_install.cmake")
  include("/home/kw-cobot/wego_ws/auto-driving-project/build/turtlebot3/turtlebot3_navigation/cmake_install.cmake")
  include("/home/kw-cobot/wego_ws/auto-driving-project/build/turtlebot3_simulations/turtlebot3_simulations/cmake_install.cmake")
  include("/home/kw-cobot/wego_ws/auto-driving-project/build/ugv_sdk/cmake_install.cmake")
  include("/home/kw-cobot/wego_ws/auto-driving-project/build/wego/cmake_install.cmake")
  include("/home/kw-cobot/wego_ws/auto-driving-project/build/hector_slam/hector_geotiff/cmake_install.cmake")
  include("/home/kw-cobot/wego_ws/auto-driving-project/build/hector_slam/hector_geotiff_plugins/cmake_install.cmake")
  include("/home/kw-cobot/wego_ws/auto-driving-project/build/hector_slam/hector_marker_drawing/cmake_install.cmake")
  include("/home/kw-cobot/wego_ws/auto-driving-project/build/navigation/map_server/cmake_install.cmake")
  include("/home/kw-cobot/wego_ws/auto-driving-project/build/scout_ros/scout_bringup/cmake_install.cmake")
  include("/home/kw-cobot/wego_ws/auto-driving-project/build/scout_ros/scout_description/cmake_install.cmake")
  include("/home/kw-cobot/wego_ws/auto-driving-project/build/timed_roslaunch/cmake_install.cmake")
  include("/home/kw-cobot/wego_ws/auto-driving-project/build/ddynamic_reconfigure/cmake_install.cmake")
  include("/home/kw-cobot/wego_ws/auto-driving-project/build/depthimage_to_laserscan/cmake_install.cmake")
  include("/home/kw-cobot/wego_ws/auto-driving-project/build/hector_slam/hector_compressed_map_transport/cmake_install.cmake")
  include("/home/kw-cobot/wego_ws/auto-driving-project/build/scout_ros/scout_base/cmake_install.cmake")
  include("/home/kw-cobot/wego_ws/auto-driving-project/build/hector_slam/hector_imu_attitude_to_tf/cmake_install.cmake")
  include("/home/kw-cobot/wego_ws/auto-driving-project/build/hector_slam/hector_imu_tools/cmake_install.cmake")
  include("/home/kw-cobot/wego_ws/auto-driving-project/build/hector_slam/hector_map_server/cmake_install.cmake")
  include("/home/kw-cobot/wego_ws/auto-driving-project/build/hector_slam/hector_trajectory_server/cmake_install.cmake")
  include("/home/kw-cobot/wego_ws/auto-driving-project/build/realsense-ros/realsense2_camera/cmake_install.cmake")
  include("/home/kw-cobot/wego_ws/auto-driving-project/build/navigation/amcl/cmake_install.cmake")
  include("/home/kw-cobot/wego_ws/auto-driving-project/build/navigation/fake_localization/cmake_install.cmake")
  include("/home/kw-cobot/wego_ws/auto-driving-project/build/hector_slam/hector_mapping/cmake_install.cmake")
  include("/home/kw-cobot/wego_ws/auto-driving-project/build/ira_laser_tools/cmake_install.cmake")
  include("/home/kw-cobot/wego_ws/auto-driving-project/build/laser_filters/cmake_install.cmake")
  include("/home/kw-cobot/wego_ws/auto-driving-project/build/turtlebot3/turtlebot3_bringup/cmake_install.cmake")
  include("/home/kw-cobot/wego_ws/auto-driving-project/build/turtlebot3/turtlebot3_example/cmake_install.cmake")
  include("/home/kw-cobot/wego_ws/auto-driving-project/build/turtlebot3_simulations/turtlebot3_fake/cmake_install.cmake")
  include("/home/kw-cobot/wego_ws/auto-driving-project/build/turtlebot3_simulations/turtlebot3_gazebo/cmake_install.cmake")
  include("/home/kw-cobot/wego_ws/auto-driving-project/build/turtlebot3/turtlebot3_slam/cmake_install.cmake")
  include("/home/kw-cobot/wego_ws/auto-driving-project/build/turtlebot3/turtlebot3_teleop/cmake_install.cmake")
  include("/home/kw-cobot/wego_ws/auto-driving-project/build/navigation/voxel_grid/cmake_install.cmake")
  include("/home/kw-cobot/wego_ws/auto-driving-project/build/navigation/costmap_2d/cmake_install.cmake")
  include("/home/kw-cobot/wego_ws/auto-driving-project/build/navigation/nav_core/cmake_install.cmake")
  include("/home/kw-cobot/wego_ws/auto-driving-project/build/navigation/base_local_planner/cmake_install.cmake")
  include("/home/kw-cobot/wego_ws/auto-driving-project/build/navigation/carrot_planner/cmake_install.cmake")
  include("/home/kw-cobot/wego_ws/auto-driving-project/build/navigation/clear_costmap_recovery/cmake_install.cmake")
  include("/home/kw-cobot/wego_ws/auto-driving-project/build/navigation/dwa_local_planner/cmake_install.cmake")
  include("/home/kw-cobot/wego_ws/auto-driving-project/build/navigation/move_slow_and_clear/cmake_install.cmake")
  include("/home/kw-cobot/wego_ws/auto-driving-project/build/navigation/navfn/cmake_install.cmake")
  include("/home/kw-cobot/wego_ws/auto-driving-project/build/navigation/global_planner/cmake_install.cmake")
  include("/home/kw-cobot/wego_ws/auto-driving-project/build/navigation/rotate_recovery/cmake_install.cmake")
  include("/home/kw-cobot/wego_ws/auto-driving-project/build/navigation/move_base/cmake_install.cmake")
  include("/home/kw-cobot/wego_ws/auto-driving-project/build/turtlebot3/turtlebot3_description/cmake_install.cmake")
  include("/home/kw-cobot/wego_ws/auto-driving-project/build/YOLOv3-ROS/yolov3_pytorch_ros/cmake_install.cmake")

endif()

if(CMAKE_INSTALL_COMPONENT)
  set(CMAKE_INSTALL_MANIFEST "install_manifest_${CMAKE_INSTALL_COMPONENT}.txt")
else()
  set(CMAKE_INSTALL_MANIFEST "install_manifest.txt")
endif()

string(REPLACE ";" "\n" CMAKE_INSTALL_MANIFEST_CONTENT
       "${CMAKE_INSTALL_MANIFEST_FILES}")
file(WRITE "/home/kw-cobot/wego_ws/auto-driving-project/build/${CMAKE_INSTALL_MANIFEST}"
     "${CMAKE_INSTALL_MANIFEST_CONTENT}")
