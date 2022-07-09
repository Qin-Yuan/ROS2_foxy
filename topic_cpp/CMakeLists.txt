cmake_minimum_required(VERSION 3.5)
project(topic_cpp)

# Default to C99
if(NOT CMAKE_C_STANDARD)
  set(CMAKE_C_STANDARD 99)
endif()

# Default to C++14
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  # the following line skips the linter which checks for copyrights
  # uncomment the line when a copyright and license is not present in all source files
  #set(ament_cmake_copyright_FOUND TRUE)
  # the following line skips cpplint (only works in a git repo)
  # uncomment the line when this package is not in a git repo
  #set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

#添加对sensor_msgs的依赖，这里没有使用sersor_msgs对变量进行定义，可以注释掉
find_package(sensor_msgs REQUIRED)
find_package(rosidl_default_generators REQUIRED)
#添加消息文件和依赖
rosidl_generate_interfaces(${PROJECT_NAME}
  "msg/Novel.msg"
   DEPENDENCIES sensor_msgs
 )


ament_package()

# 编译cpp可执行文件, cpp话题发布节点
add_executable(pub_node src/pub_cpp.cpp)
ament_target_dependencies(pub_node rclcpp)

install(TARGETS
  pub_node
  DESTINATION lib/${PROJECT_NAME}
)

# 编译cpp可执行文件, cpp话题订阅节点
add_executable(sub_node src/sub_cpp.cpp)
ament_target_dependencies(sub_node rclcpp)

install(TARGETS
  sub_node
  DESTINATION lib/${PROJECT_NAME}
)
# 添加launch可执行文件
install(DIRECTORY launch
  DESTINATION share/${PROJECT_NAME})