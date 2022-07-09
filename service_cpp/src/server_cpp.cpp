#include "rclcpp/rclcpp.hpp"
#include "my_data/srv/student.hpp"

#include <memory>

void server_callback(const std::shared_ptr<my_data::srv::Student::Request>  request,
               std::shared_ptr<my_data::srv::Student::Response> response)  {
  response->s_name = "Student_sever" ;
  response->s_num = 202 ;
  // 字符串变量使用 .c_str()函数转换
  RCLCPP_INFO(rclcpp::get_logger("rclcpp"), "server收到客户端请求，请求者信息：%s %d",
                request->c_name.c_str(), request->c_num);
}

int main(int argc, char **argv) {
  rclcpp::init(argc, argv);
  // 创建一个节点，命名为 Server_cpp
  std::shared_ptr<rclcpp::Node> node = rclcpp::Node::make_shared("Server_cpp");
  // 创建一个服务端，命名为 Student ； 当有客户端发起申请时，调用 server_callback 函数
  rclcpp::Service<my_data::srv::Student>::SharedPtr service = node->create_service<my_data::srv::Student>("Student",  &server_callback);
  RCLCPP_INFO(rclcpp::get_logger("rclcpp"), "创建一个服务端，命名为Student"); 
  rclcpp::spin(node);
  rclcpp::shutdown();
}
