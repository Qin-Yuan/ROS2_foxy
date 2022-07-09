cmake_minimum_required(VERSION 3.5)
project(service_cpp)

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

# 链接 my_data 库文件
find_package(my_data REQUIRED)

ament_package()

# 编译cpp可执行文件 服务端 server_cpp
add_executable(server_node src/server_cpp.cpp)
ament_target_dependencies(server_node rclcpp my_data)
# 将将编译好的文件安装到install/server_cpp/lib/server_node 文件下
install(TARGETS
  server_node
  DESTINATION lib/${PROJECT_NAME}
)
# 编译cpp可执行文件 服务端 client_cpp
add_executable(client_node src/client_cpp.cpp)
ament_target_dependencies(client_node rclcpp my_data)
# 将将编译好的文件安装到install/client_cpp/lib/client_node 文件下
install(TARGETS
  client_node
  DESTINATION lib/${PROJECT_NAME}
)