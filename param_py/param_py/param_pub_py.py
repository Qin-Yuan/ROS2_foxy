#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

# 话题节点类定义,继承ROS2中的类
class Param_Node(Node):
    def __init__(self,node_name):
        super().__init__(node_name)
        self.get_logger().info("创建%s节点话题发布者" % node_name)
        # 创建一个param参数, 命名为name，初始化值为 param_test
        self.declare_parameter("name", "param_test")
        self.pub = self.create_publisher(String,"pub_param",10)
        # 创建一个定时器
        time_period = 5    # 话题发布的时间周期，即触发回调函数的时间周期: 1s ；可设置为0，视为无延迟
        # 每隔1s启动一次定时器，并运行回调函数 timer_callback
        self.timer = self.create_timer(time_period, self.timer_callback)
    '''定时器回调函数初始化设置''' 
    def timer_callback(self):
        msg = String()
        # 获取param参数 name 的值,string_value为string类型，integer_value为int类型
        msg.data = self.get_parameter("name").get_parameter_value().string_value
        # 发布消息
        self.pub.publish(msg)
        # 打印发布的话题信息，可选择注释
        self.get_logger().info("发布的param信息：%s" % msg.data)
        
def main(args=None):
    # ROS2入口函数
    rclpy.init(args=args)			           # 初始化rclpy
    pub_node = Param_Node("param_pub_node")    # 新建节点，发布话题节点
    rclpy.spin(pub_node)                       # 保持节点运行，ctrl+c退出
    rclpy.shutdown()