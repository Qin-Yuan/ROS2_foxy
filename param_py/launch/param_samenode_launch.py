# 导入库
from launch import LaunchDescription
from launch_ros.actions import Node

# 定义函数名称为：generate_launch_description
def generate_launch_description():
    # 创建Actions.Node对象topic_pub , 并指出节点所在位置
    param_pub_py = Node(
        package="param_py",
        executable="param_pub_py",
        #output = 'screen',  # 可选
        parameters=[{'name': "qinyuan"}]
    )
    param_pub_py1 = Node(
        package="param_py",
        namespace="new_node",
        executable="param_pub_py",
        parameters=[{'name': "覃原"}]
    )
    # 创建LaunchDescription对象launch_description,用于描述launch文件
    launch_description = LaunchDescription([param_pub_py,param_pub_py1])
    # 返回让ROS2根据launch描述执行节点
    return launch_description