#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

class py_node(Node):
    """
    创建一个作家节点，并在初始化时输出一个话
    """
    def __init__(self,node_name):
        super().__init__(node_name)
        self.get_logger().info("%s" % node_name)


def main(args=None):
    """
    ros2运行该节点的入口函数
    1. 导入库文件
    2. 初始化客户端库
    3. 新建节点
    4. spin循环节点
    5. 关闭客户端库
    """
    rclpy.init(args=args) # 初始化rclpy
    node = py_node("ROS2_pyhton")  # 新建一个节点
    rclpy.spin(node) # 保持节点运行，检测是否收到退出指令（Ctrl+C）
    rclpy.shutdown() # 关闭rclpy

