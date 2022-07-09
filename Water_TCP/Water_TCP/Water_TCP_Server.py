#!/usr/bin/env python3
from my_data.srv import Watercmd       # request_cmd ； response_cmd
from rclpy.node import Node
import socket
import rclpy

class Watercmd_Node(Node):
    def __init__(self):
        super().__init__('Watercmd_Node')
        # 新建两个参数 Water_IP 、Water_PORT , 初始化默认如下
        self.declare_parameter("Water_IP", "192.168.10.10")
        self.declare_parameter("Water_PORT", 31001)

        # TCP调试助手测试
        # self.declare_parameter("Water_IP", "192.168.1.109")
        # self.declare_parameter("Water_PORT", 8080)

        self.get_logger().info("向移动底盘发起连接！")
        # 尝试连接移动底盘客户端
        self.Water_client()

    ''' TCP Client '''
    def Water_client(self):
        # 获取参数的 IP地址 和 端口号
        HOST = self.get_parameter("Water_IP").get_parameter_value().string_value
        PORT  = self.get_parameter("Water_PORT").get_parameter_value().integer_value
        # 设置超时时间
        socket.setdefaulttimeout(5)
        # 创建一个客户端用于连接到移动底盘
        self.Water_Client = socket.socket(
            socket.AF_INET, 
            socket.SOCK_STREAM
        )
        try :
            self.Water_Client.connect((HOST,PORT))
        except  Exception as e :
            self.get_logger().error("链接失败，请检查IP地址和端口号是否正确；移动设备是否开机！")
            rclpy.shutdown()
        else :
            self.get_logger().info("连接成功")
            self.srv = self.create_service(Watercmd, 'Water_cmd', self.Services_callback)

    ''' 回调函数 '''
    def Services_callback(self, request, response):
        cmd = request.request_cmd
        
        # 非结束指令
        if cmd != "over" :
            self.get_logger().info('接受到指令: %s' % (cmd))    
            # 发送指令给移动底盘        
            self.Water_Client.send(cmd.encode('utf-8'))
            # 接受指令反馈
            response.response_cmd = self.Water_Client.recv(1024).decode('utf-8')
        
        # 结束指令
        if cmd == "over" :
            response.response_cmd = "OK"
            # 关闭时取消机器人的所有操作
            Close = "/api/move/cancel"
            self.Water_Client.send(Close.encode('utf-8'))
            self.get_logger().info('接受到指令: %s , 即将机器人所有操作！' % (request.request_cmd))
               
        return response

def main(args=None):
    rclpy.init(args=args)
    Watercmd_node = Watercmd_Node()
    rclpy.spin(Watercmd_node)
    rclpy.shutdown()