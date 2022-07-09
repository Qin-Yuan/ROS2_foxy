from setuptools import setup
# 启动launch文件依赖 
from glob import glob
import os

package_name = 'param_py'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        # launch文件添加 , glob 需要修改成自己定义的后缀句型
        (os.path.join('share', package_name, 'launch'), glob('launch/*_launch.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='qys',
    maintainer_email='qys@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "param_pub_py = param_py.param_pub_py:main"
        ],
    },
)
