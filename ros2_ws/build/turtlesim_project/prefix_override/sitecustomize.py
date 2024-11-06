import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/ayush/Desktop/Learning_ROS2/ros2_ws/install/turtlesim_project'
