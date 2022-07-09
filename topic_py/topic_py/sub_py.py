#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class Topic_Node(Node):
    def __init__(self,node_name):
        super().__init__(node_name)
        self.get_logger().info("创建%s节点话题订阅者" % node_name)
        # 创建一个话题订阅者
        self.sub = self.create_subscription(String,"pub_msgs",self.sub_callback,10)
    def sub_callback(self,data):
        self.msgs = data.data
        self.get_logger().info("订阅话题信息：%s" % self.msgs)
        
def main(args=None):
    # ROS2入口函数
    rclpy.init(args=args)			     # 初始化rclpy
    sub_node = Topic_Node("sub_node")    # 新建节点，订阅话题节点
    rclpy.spin(sub_node)                 # 保持节点运行，ctrl+c退出
    rclpy.shutdown()