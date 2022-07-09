#!/usr/bin/env python3
from my_data.srv import Student       # 导入自定义的 srv 文件 
import rclpy
from rclpy.node import Node

# 客户端节点类
class Service_Node(Node):
    def __init__(self):
        super().__init__('Service_node')
        # 创建一个服务端节点，数据类型为Student, 服务名称为 server_py, 客户端请求时触发回调函数
        self.srv = self.create_service(Student, 'server_py', self.Services_callback)
    # 定义回调函数，request为客户端发送的请求，response为服务端的响应
    def Services_callback(self, request, response):
        response.s_name = "Student_server"
        response.s_num = 101
        # 打印日志
        self.get_logger().info('服务端接收到请求，请求人信息： %s  %d' % (request.c_name, request.c_num))
        # 对客户端的反馈回应
        return response


def main(args=None):
    rclpy.init(args=args)
    # 服务端类节点实例化
    service_node = Service_Node()
    rclpy.spin(service_node)
    rclpy.shutdown()