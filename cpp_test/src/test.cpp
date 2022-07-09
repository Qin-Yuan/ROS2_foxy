#include "rclcpp/rclcpp.hpp"

/*
    创建一个类节点，名字叫做cpp_test,继承自Node.
*/
class cpp_node : public rclcpp::Node {
    public:
        // 构造函数,有一个参数为节点名称
        cpp_node(std::string name) : Node(name) {
            // 打印一句自我介绍
            RCLCPP_INFO(this->get_logger(), "%s",name.c_str());
        }
    private:
   
};

int main(int argc, char **argv) {
    rclcpp::init(argc, argv);
    /*产生一个cpp_node的节点*/
    auto node = std::make_shared<cpp_node>("cpp_node");
    /* 运行节点，并检测退出信号*/
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}
