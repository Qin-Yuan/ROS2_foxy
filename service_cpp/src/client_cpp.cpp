#include "rclcpp/rclcpp.hpp"
#include "my_data/srv/student.hpp"

#include <chrono>
#include <cstdlib>
#include <memory>

using namespace std::chrono_literals;

int main(int argc, char **argv) {
  rclcpp::init(argc, argv);
  // 创建一个 ROS 节点，命名为 Client_cpp
  std::shared_ptr<rclcpp::Node> node = rclcpp::Node::make_shared("Client_cpp"); 
  // 创建一个客户端client，向名为Student的服务端发起申请
  rclcpp::Client<my_data::srv::Student>::SharedPtr client = node->create_client<my_data::srv::Student>("Student");                  
  auto request = std::make_shared<my_data::srv::Student::Request>();              
  request->c_name = "Student_client" ;
  request->c_num = 101 ;

  while (!client->wait_for_service(1s)) {
    if (!rclcpp::ok()) {
      RCLCPP_ERROR(rclcpp::get_logger("rclcpp"), "程序异常，无法连接到服务端！");
      return 0;
    }
    RCLCPP_WARN(rclcpp::get_logger("rclcpp"), "服务端正忙，稍后再试！");
  }
  // 向服务端发送请求
  auto result = client->async_send_request(request);
  // 等待服务端的响应
  if (rclcpp::spin_until_future_complete(node, result) == rclcpp::executor::FutureReturnCode::SUCCESS) {
    // 打印服务端的反馈数据
    RCLCPP_INFO(rclcpp::get_logger("rclcpp"), "Client接受到服务端的反馈： %s  %d", result.get()->s_name.c_str(),result.get()->s_num);
  } else {
    RCLCPP_ERROR(rclcpp::get_logger("rclcpp"), "程序异常，无法连接到服务端！");
  }
  rclcpp::shutdown();
  return 0;
}