import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/yuxuan/ros2_ws/src/ROS2_wear/install/ROS2_wear'
