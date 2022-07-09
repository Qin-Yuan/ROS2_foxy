#!/usr/bin/env python3
from my_data.srv import Student
import rclpy
from rclpy.node import Node

# 定义客户端类节点
class Client_Node(Node):
    def __init__(self):
        super().__init__('Client_Node')
        # 创建一个客户端，数据类型为Student, 向名为server_py客户端发起请求
        self.cli = self.create_client(Student,"server_py")
        # 超时响应时打印日志
        while not self.cli.wait_for_service(timeout_sec=1):
            self.get_logger().warn('服务端正忙，稍后在申请！')
        self.req = Student.Request()
    # 发送请求
    def send_request(self):
        # 对 srv 数据赋值
        self.req.c_name = "Student_client"
        self.req.c_num  = 202
        # 向服务端发送请求
        self.future = self.cli.call_async(self.req)


def main(args=None):
    rclpy.init(args=args)
    # 客户端类的实例化
    client_node = Client_Node()
    # 发送请求
    client_node.send_request()
    while rclpy.ok():
        # 循环一次
        rclpy.spin_once(client_node)
        # 客户端连接是否成功
        if client_node.future.done():
            try:
                # 获取客户端的反馈信息
                response = client_node.future.result()
            except Exception as e:
                client_node.get_logger().error(
                    'client发送申请失败 %r' % (e,))
            else:
                client_node.get_logger().info(
                    'Client接收到服务端反馈: %s  %d' % (response.s_name, response.s_num)
                )
            break
    # 关闭节点
    client_node.destroy_node()
    rclpy.shutdown()