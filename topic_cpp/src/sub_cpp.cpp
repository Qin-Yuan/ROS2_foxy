#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/string.hpp"
using std::placeholders::_1;        // 回调函数的参数个数，_1 表示一个
using std::placeholders::_2;        // 回调函数的参数个数，_2 表示两个； 可以设置更多

class sub_node:public rclcpp::Node {
  public:
    sub_node():Node("sub_node") {
        // 创建话题订阅者，订阅话题名为 pub_msgs ； 接受到话题信息后触发回调函数
        subscription_ = this->create_subscription<std_msgs::msg::String>(
        "pub_msgs", 10, std::bind(&sub_node::sub_callback, this, _1));
    }

  private:
    void sub_callback(const std_msgs::msg::String::SharedPtr msg) const {
        // this->get_logger() ROS2日志时间戳
        RCLCPP_INFO(this->get_logger(), "sub_node的订阅话题信息: '%s'", msg->data.c_str());
    }
    // 初始化订阅者变量
    rclcpp::Subscription<std_msgs::msg::String>::SharedPtr subscription_;
};

int main(int argc, char * argv[]) {
    rclcpp::init(argc, argv);
    // 循环订阅节点
    rclcpp::spin(std::make_shared<sub_node>());
    rclcpp::shutdown();
    return 0;
}