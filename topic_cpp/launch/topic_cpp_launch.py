# 导入库
from launch import LaunchDescription
from launch_ros.actions import Node

# 定义函数名称为：generate_launch_description
def generate_launch_description():
    # 创建Actions.Node对象topic_pub , 并指出节点所在位置
    topic_pub = Node(
        package="topic_cpp",
        # 下面是CMakeLists.txt文件中将cpp文件定义的节点名称，不是可执行cpp文件的名称
        executable="pub_node"
        )
    # 创建Actions.Node对象topic_sub , 并指出节点所在位置
    topic_sub = Node(
        package="topic_cpp",
        executable="sub_node"
        )
    # 创建LaunchDescription对象launch_description,用于描述launch文件
    launch_description = LaunchDescription([topic_pub,topic_sub])
    # 返回让ROS2根据launch描述执行节点
    return launch_description