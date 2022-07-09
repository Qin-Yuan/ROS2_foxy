#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/string.hpp"

using namespace std::chrono_literals;

/* 定义一个节点发布的类，继承 rclcpp::Node */
class param_pub_node : public rclcpp::Node {
  public:
    param_pub_node():Node("pub_cpp"), count_(0) {
        RCLCPP_INFO(this->get_logger(), "创建话题发布者pub_param节点");
        publisher_ = this->create_publisher<std_msgs::msg::String>("pub_param", 10);
        // 创建一个param参数，命名为name, 初始化“param_test”
        this->declare_parameter<std::string>("name" , "param_test");
        // 新建一个定时器，500ms触发一次回调函数；这里的时间可以是秒s、毫秒ms
        timer_ = this->create_wall_timer(
            5s, std::bind(&param_pub_node::timer_callback, this));
    }
  private:
    // 定义定时器触发的回调函数
    void timer_callback() {
        auto msgs = std_msgs::msg::String();
        // 获取 param 参数并赋值给 msgs.data
        this->get_parameter("name" , msgs.data) ;
        // C++日志打印输出
        RCLCPP_INFO(this->get_logger(), "param_pub_cpp发布的参数信息: '%s'", msgs.data.c_str());
        // 话题发布
        publisher_->publish(msgs);
    }
    // 初始化创建变量
    rclcpp::TimerBase::SharedPtr timer_;
    rclcpp::Publisher<std_msgs::msg::String>::SharedPtr publisher_;
    size_t count_;
};

int main(int argc, char * argv[]) {
    // 初始化节点
    rclcpp::init(argc, argv) ;
    // 循环节点
    rclcpp::spin(std::make_shared<param_pub_node>()) ;
    rclcpp::shutdown() ;
    return 0;
}