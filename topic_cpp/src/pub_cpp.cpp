#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/string.hpp"

using namespace std::chrono_literals;

/* 定义一个节点发布的类，继承 rclcpp::Node */
class pub_node : public rclcpp::Node {
  public:
    pub_node():Node("pub_cpp"), count_(0) {
      // RCLCPP_INFO(this->get_logger(), "public");
      // 新建一个发布者，发布话题为 pub_msgs
      publisher_ = this->create_publisher<std_msgs::msg::String>("pub_msgs", 10);
      // 新建一个定时器，500ms触发一次回调函数；这里的时间可以是秒s、毫秒ms
      timer_ = this->create_wall_timer(
        2s, std::bind(&pub_node::timer_callback, this));
    }
  private:
    // 定义定时器触发的回调函数
    void timer_callback() {
      // RCLCPP_INFO(this->get_logger(), "private");
      // 字符串变量
      auto msgs = std_msgs::msg::String();
      // 字符串数据赋值，并将 count__计数自加1
      msgs.data = "Hello, world! " + std::to_string(count_++);
      // C++日志打印输出
      RCLCPP_INFO(this->get_logger(), "pub_cpp发布的话题信息: '%s'", msgs.data.c_str());
      // 话题发布
      publisher_->publish(msgs);
    }
    // 初始化创建变量
    rclcpp::TimerBase::SharedPtr timer_ ;
    rclcpp::Publisher<std_msgs::msg::String>::SharedPtr publisher_ ;
    size_t count_;
};

int main(int argc, char * argv[]) {
  // 初始化节点
  rclcpp::init(argc, argv) ;
  // 循环节点
  rclcpp::spin(std::make_shared<pub_node>()) ;
  rclcpp::shutdown() ;
  return 0;
}